
# Created by admin at 8/10/2026
Feature: Test case for Target Cart

  Scenario: User can verify cart is empty
    Given Open target main page for cart
    When Click on cart icon
    Then Verify "Your cart is empty" message is shown