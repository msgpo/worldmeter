from worldmeter.coronavirus import CovidMeter

c = CovidMeter()

data = c.global_data()
"""
{'active_cases': 109014,
 'country': 'world',
 'critical': 6099,
 'date': '2020/03/16',
 'new_cases': 7347,
 'new_deaths': 220,
 'total_cases': 195211,
 'total_deaths': 7006,
 'total_recovered': 79191}
"""

data = c.get_country_data("Portugal")  # country names, NOT country code
"""
{'active_cases': 327,
 'cases_per_1M': 32.5,
 'country': 'Portugal',
 'critical': 18,
 'date': '2020/03/16',
 'new_cases': 86,
 'new_deaths': 1,
 'total_cases': 331,
 'total_deaths': 1,
 'total_recovered': 3}
"""