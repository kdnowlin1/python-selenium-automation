# Created by admin at 8/10/2026
Feature: Test case for Target Signin

  Scenario: User can navigate to Sign In:
    Given Open main target page
    When Click Sign In
    When Click Sign In from navigation menu
    Then Verify Sign In form opened
