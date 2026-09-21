# aircraft_catalog.py


def aircraft_catalog() -> list:
    aircraft_catalog_list = [
        {
            "manufacturer": "Airbus",
            "model": "A340-300",
            "required_crew": 10,
            "optimal_range_km": 3_400,
            "financials": {
                "price": 70_000_000,
                "annual_maintenance_cost": 3_500_000,
                "daily_operating_cost": 68_000,
                "daily_net_profit": 51_000,
            },
            "operations_24h": {"flights_per_24h": 1},
            "environmental_impact": {
                "co2_emissions_per_km": 12.5,
                "co2_rating": 4.0,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A318",
            "required_crew": 5,
            "optimal_range_km": 150,
            "financials": {
                "price": 77_400_000,
                "annual_maintenance_cost": 1_200_000,
                "daily_operating_cost": 18_000,
                "daily_net_profit": 36_000,
            },
            "operations_24h": {"flights_per_24h": 6},
            "environmental_impact": {
                "co2_emissions_per_km": 7.8,
                "co2_rating": 5.0,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A330-200",
            "required_crew": 11,
            "optimal_range_km": 1_850,
            "financials": {
                "price": 238_500_000,
                "annual_maintenance_cost": 2_200_000,
                "daily_operating_cost": 76_000,
                "daily_net_profit": 130_000,
            },
            "operations_24h": {"flights_per_24h": 2},
            "environmental_impact": {
                "co2_emissions_per_km": 11.2,
                "co2_rating": 6.4,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A320ceo",
            "required_crew": 6,
            "optimal_range_km": 700,
            "financials": {
                "price": 101_000_000,
                "annual_maintenance_cost": 1_100_000,
                "daily_operating_cost": 33_000,
                "daily_net_profit": 60_000,
            },
            "operations_24h": {"flights_per_24h": 3},
            "environmental_impact": {
                "co2_emissions_per_km": 6.8,
                "co2_rating": 7.0,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A380-800",
            "required_crew": 21,
            "optimal_range_km": 4_500,
            "financials": {
                "price": 445_600_000,
                "annual_maintenance_cost": 6_000_000,
                "daily_operating_cost": 115_000,
                "daily_net_profit": 290_000,
            },
            "operations_24h": {"flights_per_24h": 1},
            "environmental_impact": {
                "co2_emissions_per_km": 22.0,
                "co2_rating": 7.3,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A330-900neo",
            "required_crew": 10,
            "optimal_range_km": 3_400,
            "financials": {
                "price": 296_400_000,
                "annual_maintenance_cost": 1_800_000,
                "daily_operating_cost": 48_000,
                "daily_net_profit": 153_000,
            },
            "operations_24h": {"flights_per_24h": 1},
            "environmental_impact": {
                "co2_emissions_per_km": 9.5,
                "co2_rating": 8.2,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A350-900",
            "required_crew": 11,
            "optimal_range_km": 4_500,
            "financials": {
                "price": 317_400_000,
                "annual_maintenance_cost": 1_900_000,
                "daily_operating_cost": 62_000,
                "daily_net_profit": 235_000,
            },
            "operations_24h": {"flights_per_24h": 1},
            "environmental_impact": {
                "co2_emissions_per_km": 9.0,
                "co2_rating": 8.6,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A320neo",
            "required_crew": 6,
            "optimal_range_km": 820,
            "financials": {
                "price": 110_600_000,
                "annual_maintenance_cost": 900_000,
                "daily_operating_cost": 28_500,
                "daily_net_profit": 75_000,
            },
            "operations_24h": {"flights_per_24h": 3},
            "environmental_impact": {
                "co2_emissions_per_km": 5.7,
                "co2_rating": 9.2,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A220-300",
            "required_crew": 5,
            "optimal_range_km": 510,
            "financials": {
                "price": 91_500_000,
                "annual_maintenance_cost": 750_000,
                "daily_operating_cost": 24_600,
                "daily_net_profit": 72_000,
            },
            "operations_24h": {"flights_per_24h": 4},
            "environmental_impact": {
                "co2_emissions_per_km": 4.8,
                "co2_rating": 9.6,
            },
        },
        {
            "manufacturer": "Airbus",
            "model": "A321neo",
            "required_crew": 7,
            "optimal_range_km": 1_900,
            "financials": {
                "price": 129_500_000,
                "annual_maintenance_cost": 950_000,
                "daily_operating_cost": 32_000,
                "daily_net_profit": 102_000,
            },
            "operations_24h": {"flights_per_24h": 2},
            "environmental_impact": {
                "co2_emissions_per_km": 5.2,
                "co2_rating": 9.8,
            },
        },
    ]

    return aircraft_catalog_list


def print_aircraft_catalog_table(aircraft_catalog: list):
    header = (
        f"| {'Manufacturer':<12} | {'Model':<12} | {'Crew':<5} | {'Range(km)':<10} "
        f"| {'Price (€)':<14} | {'CO2/km':<8} | {'CO2 Rating':<10} |"
    )
    divider = "-" * len(header)

    print("\n" + divider)
    print(header)
    print(divider)

    for aircraft in aircraft_catalog:
        mfr = aircraft["manufacturer"]
        model = aircraft["model"]
        crew = aircraft["required_crew"]
        opt_range = aircraft["optimal_range_km"]
        price = aircraft["financials"]["price"]
        co2_km = aircraft["environmental_impact"]["co2_emissions_per_km"]
        co2_rating = aircraft["environmental_impact"]["co2_rating"]

        print(
            f"| {mfr:<12} | {model:<12} | {crew:<5} | {opt_range:<10,} "
            f"| {price:<14,} | {co2_km:<8.1f} | {co2_rating:<10.1f} |"
        )

    print(divider + "\n")