import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from car import Car

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def test_start_and_accelerate():
    c = Car("Volvo", "XC90", 2023)
    assert c.engine_on is False
    msg = c.start_engine()
    assert "har startat" in msg
    out = c.accelerate(60)
    assert c.current_speed == 60
    assert "Hastighet: 60" in out

def test_brake_and_status():
    c = Car("Tesla", "Model 3", 2022)
    c.start_engine(); c.accelerate(100)
    s = c.brake(70)
    assert "Ny hastighet: 30" in s
    status = c.get_status()
    assert "Motor: På" in status and "Hastighet: 30" in status

def run_tests():
    """Run all tests and display results with a nice UI"""
    tests = [
        ("test_start_and_accelerate", test_start_and_accelerate),
        ("test_brake_and_status", test_brake_and_status),
    ]
    
    passed = []
    failed = []
    
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{'TEST RUNNER':^60}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed.append(test_name)
            print(f"{GREEN}✓{RESET} {BOLD}{test_name}{RESET} {GREEN}PASSED{RESET}")
        except AssertionError as e:
            failed.append((test_name, str(e)))
            print(f"{RED}✗{RESET} {BOLD}{test_name}{RESET} {RED}FAILED{RESET}")
            print(f"   {RED}Error: {str(e)}{RESET}")
        except Exception as e:
            failed.append((test_name, str(e)))
            print(f"{RED}✗{RESET} {BOLD}{test_name}{RESET} {RED}FAILED{RESET}")
            print(f"   {RED}Unexpected error: {str(e)}{RESET}")
    
    # Summary
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}SUMMARY{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    total = len(tests)
    passed_count = len(passed)
    failed_count = len(failed)
    
    print(f"\n{GREEN}Passed: {passed_count}/{total}{RESET}")
    if failed:
        print(f"{RED}Failed: {failed_count}/{total}{RESET}\n")
        print(f"{BOLD}Failed Tests:{RESET}")
        for test_name, error in failed:
            print(f"  {RED}• {test_name}{RESET}")
            print(f"    {error}")
    else:
        print(f"{RED}Failed: 0/{total}{RESET}")
    
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    
    if failed:
        print(f"\n{BOLD}{RED}❌ SOME TESTS FAILED{RESET}")
        return 1
    else:
        print(f"\n{BOLD}{GREEN}✅ ALL TESTS PASSED{RESET}")
        return 0

if __name__ == "__main__":
    sys.exit(run_tests())
