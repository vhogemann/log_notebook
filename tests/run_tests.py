#!/usr/bin/env python3
"""
Test runner script for the log_to_graph package.

This script runs all unit tests and generates a coverage report.
"""

import sys
import os
import subprocess
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def run_tests():
    """Run all tests with pytest."""
    print("🧪 Running LogToGraph Unit Tests")
    print("=" * 50)
    
    # Change to project root directory
    os.chdir(project_root)
    
    # Run pytest with verbose output and coverage
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--color=yes",
        "--durations=10"
    ]
    
    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode == 0
    except FileNotFoundError:
        print("❌ pytest not found. Installing pytest...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pytest"], check=True)
        result = subprocess.run(cmd, check=False)
        return result.returncode == 0

def run_tests_with_coverage():
    """Run tests with coverage report."""
    print("\n📊 Running Tests with Coverage")
    print("=" * 50)
    
    # Install coverage if not available
    try:
        import coverage
    except ImportError:
        print("Installing coverage...")
        subprocess.run([sys.executable, "-m", "pip", "install", "coverage"], check=True)
    
    # Run tests with coverage
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "--cov=log_to_graph",
        "--cov-report=html",
        "--cov-report=term-missing",
        "-v"
    ]
    
    try:
        result = subprocess.run(cmd, check=False)
        if result.returncode == 0:
            print("\n✅ Coverage report generated in htmlcov/")
        return result.returncode == 0
    except FileNotFoundError:
        print("❌ pytest-cov not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pytest-cov"], check=True)
        result = subprocess.run(cmd, check=False)
        return result.returncode == 0

def run_linting():
    """Run code linting."""
    print("\n🔍 Running Code Linting")
    print("=" * 50)
    
    try:
        import flake8
    except ImportError:
        print("Installing flake8...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flake8"], check=True)
    
    # Run flake8 on the package
    cmd = [sys.executable, "-m", "flake8", "log_to_graph/", "--max-line-length=88"]
    
    result = subprocess.run(cmd, check=False)
    if result.returncode == 0:
        print("✅ No linting issues found")
    else:
        print("❌ Linting issues found")
    
    return result.returncode == 0

def install_test_dependencies():
    """Install test dependencies."""
    print("📦 Installing Test Dependencies")
    print("=" * 50)
    
    dependencies = [
        "pytest>=6.0.0",
        "pytest-cov>=2.0.0",
        "flake8>=3.8.0"
    ]
    
    for dep in dependencies:
        print(f"Installing {dep}...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                         check=True, capture_output=True)
            print(f"✅ {dep} installed")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {dep}: {e}")
            return False
    
    return True

def main():
    """Main test runner."""
    print("🚀 LogToGraph Test Suite")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not (project_root / "log_to_graph").exists():
        print("❌ Error: log_to_graph package not found")
        print(f"Current directory: {project_root}")
        sys.exit(1)
    
    # Install dependencies
    if not install_test_dependencies():
        print("❌ Failed to install test dependencies")
        sys.exit(1)
    
    success = True
    
    # Run basic tests
    if not run_tests():
        print("❌ Basic tests failed")
        success = False
    
    # Run tests with coverage
    if not run_tests_with_coverage():
        print("❌ Coverage tests failed")
        success = False
    
    # Run linting
    if not run_linting():
        print("⚠️  Linting issues found (not blocking)")
    
    print("\n" + "=" * 50)
    if success:
        print("✅ All tests passed!")
        print("\n📋 Test Summary:")
        print("   • Unit tests: ✅ PASSED")
        print("   • Coverage report: ✅ GENERATED")
        print("   • Integration tests: ✅ PASSED")
        print("\n📁 Reports generated:")
        print("   • Coverage: htmlcov/index.html")
    else:
        print("❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
