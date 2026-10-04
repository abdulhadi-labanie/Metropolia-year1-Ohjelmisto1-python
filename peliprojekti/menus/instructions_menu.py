from utils import read_str_input, clear_screen

def instructions_menu_switcher():
    read_str_input("\n> Enter any key to return Main Menu: ")
    return

def show_instructions_menu():
    print("\n" + "="*50 + " GAME INSTRUCTIONS & GUIDE " + "="*50)
    print("\n1. [Game Idea & Goal]:")
    print("   You are an airline manager. Your goal is to buy aircraft, assign profitable routes,")
    print("   and maximize annual profit while keeping emissions low.")
    print("   * Example: Buying an Airbus A320 and managing its operations successfully.")
    print("\n2. [How Algorithms Work]:")
    print("   - Flights & Duration: Calculated using plane speed (800 km/h) and distance.")
    print("     * Example: A 500 km trip takes about 2 hours per round including turnaround time.")
    print("   - Passengers & Profit: Based on seat capacity, ticket price, and operating costs.")
    print("     * Example: Revenue minus [Maintenance + (Daily Cost * 365)] = Net Profit.")
    print("   - Risks: Failed landings depend on weather severity and runway conditions.")
    print("\n3. [How to Get an Excellent CO2 Rating]:")
    print("   - Range Matching is Key: The closer the destination distance is to your plane's optimal range,")
    print("     the higher your efficiency and CO2 rating will be.")
    print("     * Good Example: Using an A321neo (Range ~1900 km) for a trip to Istanbul (1730 km) -> High CO2 Rating (~85%).")
    print("     * Bad Example: Using a giant A380 for a short domestic flight -> Massive range penalty & low rating (~5%).")
    print("="*127 + "\n")

def instructions_menu():
    clear_screen()
    show_instructions_menu()
    instructions_menu_switcher()
