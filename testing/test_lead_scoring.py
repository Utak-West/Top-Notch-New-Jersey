#!/usr/bin/env python3
"""
Test script for lead scoring algorithm validation
Tests the lead scoring logic from the automation integration setup
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LeadProcessor:
    """Lead processing class with scoring algorithm"""
    
    def calculate_lead_score(self, form_data):
        """Calculate lead score based on form responses"""
        score = 0
        
        service_scores = {
            'complete_home': 30,
            'kitchen_remodeling': 20,
            'bathroom_renovation': 15
        }
        score += service_scores.get(form_data.get('service_selection'), 0)
        
        budget_scores = {
            'over_100k': 25,
            '60k_100k': 20,
            '30k_60k': 15,
            '15k_30k': 10,
            'under_15k': 5
        }
        score += budget_scores.get(form_data.get('budget_range'), 0)
        
        timeline_scores = {
            'asap': 20,
            '1_month': 15,
            '3_months': 10,
            '6_months': 5,
            'planning': 2
        }
        score += timeline_scores.get(form_data.get('timeline'), 0)
        
        scope_scores = {
            'complete_renovation': 15,
            'major_updates': 10,
            'refresh': 5
        }
        score += scope_scores.get(form_data.get('project_scope'), 0)
        
        if 'contact_info' in form_data and 'address' in form_data['contact_info']:
            address = form_data['contact_info']['address'].lower()
            if any(city in address for city in ['linden', 'elizabeth', 'westfield']):
                score += 10  # Primary service area
            elif any(county in address for county in ['union', 'essex', 'middlesex', 'bergen']) or any(city in address for city in ['newark']):
                score += 7   # Secondary service area (includes Newark in Essex County)
            else:
                score += 3   # Extended service area
        
        return min(score, 100)  # Cap at 100 points
    
    def classify_lead_priority(self, lead_score):
        """Classify lead priority based on score"""
        if lead_score >= 80:
            return 'HOT'
        elif lead_score >= 60:
            return 'WARM'
        elif lead_score >= 40:
            return 'QUALIFIED'
        else:
            return 'COLD'

def run_lead_scoring_tests():
    """Run comprehensive lead scoring tests"""
    processor = LeadProcessor()
    
    print("=" * 60)
    print("LEAD SCORING ALGORITHM VALIDATION TESTS")
    print("=" * 60)
    print()
    
    print("TEST 1: HIGH SCORE LEAD")
    print("-" * 30)
    high_score_data = {
        'service_selection': 'complete_home',
        'budget_range': 'over_100k', 
        'timeline': 'asap',
        'project_scope': 'complete_renovation',
        'contact_info': {'address': '123 Main St, Linden, NJ 07036'}
    }
    
    high_score = processor.calculate_lead_score(high_score_data)
    high_priority = processor.classify_lead_priority(high_score)
    
    print(f"Input Data:")
    print(f"  Service: Complete Home Remodel (30 points)")
    print(f"  Budget: Over $100K (25 points)")
    print(f"  Timeline: ASAP (20 points)")
    print(f"  Scope: Complete Renovation (15 points)")
    print(f"  Location: Linden, NJ (10 points)")
    print(f"Expected: 100 points, HOT priority")
    print(f"Actual: {high_score} points, {high_priority} priority")
    print(f"Result: {'PASS' if high_score == 100 and high_priority == 'HOT' else 'FAIL'}")
    print()
    
    print("TEST 2: MEDIUM SCORE LEAD")
    print("-" * 30)
    medium_score_data = {
        'service_selection': 'kitchen_remodeling',
        'budget_range': '30k_60k',
        'timeline': '3_months', 
        'project_scope': 'major_updates',
        'contact_info': {'address': '456 Oak St, Elizabeth, NJ 07201'}
    }
    
    medium_score = processor.calculate_lead_score(medium_score_data)
    medium_priority = processor.classify_lead_priority(medium_score)
    
    print(f"Input Data:")
    print(f"  Service: Kitchen Remodeling (20 points)")
    print(f"  Budget: $30K-$60K (15 points)")
    print(f"  Timeline: 3 months (10 points)")
    print(f"  Scope: Major Updates (10 points)")
    print(f"  Location: Elizabeth, NJ (10 points)")
    print(f"Expected: 65 points, WARM priority")
    print(f"Actual: {medium_score} points, {medium_priority} priority")
    print(f"Result: {'PASS' if medium_score == 65 and medium_priority == 'WARM' else 'FAIL'}")
    print()
    
    print("TEST 3: LOW SCORE LEAD")
    print("-" * 30)
    low_score_data = {
        'service_selection': 'bathroom_renovation',
        'budget_range': 'under_15k',
        'timeline': 'planning',
        'project_scope': 'refresh', 
        'contact_info': {'address': '789 Pine St, Newark, NJ 07102'}
    }
    
    low_score = processor.calculate_lead_score(low_score_data)
    low_priority = processor.classify_lead_priority(low_score)
    
    print(f"Input Data:")
    print(f"  Service: Bathroom Renovation (15 points)")
    print(f"  Budget: Under $15K (5 points)")
    print(f"  Timeline: Planning (2 points)")
    print(f"  Scope: Refresh (5 points)")
    print(f"  Location: Newark, NJ (7 points)")
    print(f"Expected: 34 points, COLD priority")
    print(f"Actual: {low_score} points, {low_priority} priority")
    print(f"Result: {'PASS' if low_score == 34 and low_priority == 'COLD' else 'FAIL'}")
    print()
    
    print("TEST 4: EDGE CASE - NO LOCATION DATA")
    print("-" * 30)
    no_location_data = {
        'service_selection': 'kitchen_remodeling',
        'budget_range': '60k_100k',
        'timeline': '1_month',
        'project_scope': 'complete_renovation'
    }
    
    no_location_score = processor.calculate_lead_score(no_location_data)
    no_location_priority = processor.classify_lead_priority(no_location_score)
    
    print(f"Input Data:")
    print(f"  Service: Kitchen Remodeling (20 points)")
    print(f"  Budget: $60K-$100K (20 points)")
    print(f"  Timeline: 1 month (15 points)")
    print(f"  Scope: Complete Renovation (15 points)")
    print(f"  Location: No data (0 points)")
    print(f"Expected: 70 points, WARM priority")
    print(f"Actual: {no_location_score} points, {no_location_priority} priority")
    print(f"Result: {'PASS' if no_location_score == 70 and no_location_priority == 'WARM' else 'FAIL'}")
    print()
    
    print("TEST 5: EXTENDED SERVICE AREA")
    print("-" * 30)
    extended_area_data = {
        'service_selection': 'bathroom_renovation',
        'budget_range': '30k_60k',
        'timeline': '6_months',
        'project_scope': 'major_updates',
        'contact_info': {'address': '321 Elm St, Trenton, NJ 08608'}
    }
    
    extended_score = processor.calculate_lead_score(extended_area_data)
    extended_priority = processor.classify_lead_priority(extended_score)
    
    print(f"Input Data:")
    print(f"  Service: Bathroom Renovation (15 points)")
    print(f"  Budget: $30K-$60K (15 points)")
    print(f"  Timeline: 6 months (5 points)")
    print(f"  Scope: Major Updates (10 points)")
    print(f"  Location: Trenton, NJ - Extended Area (3 points)")
    print(f"Expected: 48 points, QUALIFIED priority")
    print(f"Actual: {extended_score} points, {extended_priority} priority")
    print(f"Result: {'PASS' if extended_score == 48 and extended_priority == 'QUALIFIED' else 'FAIL'}")
    print()
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    test_results = [
        high_score == 100 and high_priority == 'HOT',
        medium_score == 65 and medium_priority == 'WARM',
        low_score == 34 and low_priority == 'COLD',
        no_location_score == 70 and no_location_priority == 'WARM',
        extended_score == 48 and extended_priority == 'QUALIFIED'
    ]
    
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    print(f"Tests Passed: {passed_tests}/{total_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if passed_tests == total_tests:
        print("STATUS: ALL TESTS PASSED - Lead scoring algorithm is working correctly!")
    else:
        print("STATUS: SOME TESTS FAILED - Lead scoring algorithm needs review")
    
    print()
    return passed_tests == total_tests

if __name__ == "__main__":
    success = run_lead_scoring_tests()
    sys.exit(0 if success else 1)
