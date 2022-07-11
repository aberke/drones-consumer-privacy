

# Attribute levels.
# Assumed:
# All vendors have the same number of levels for each attribute.
# Except for drone privacy.
# Attribute levels are the same for drone and ground vehicles.

VENDOR_TYPES = [
    'take-out food', 
    'prescription medications',
    ''
]

# Delivery fee
COST_LEVELS = [
    [(0, "$0"), (1, "$1"), (3, "$3"), (5, "$5")],
    [(0, "$0"), (1, "$1"), (5, "$5"), (10, "$10")],
    [],
]

# Delivery wait time in minutes
TIME_LEVELS = [
    [(15, "15 minutes"), (20, "20 minutes"), (30, "30 minutes"), (45, "45 minutes")],
    [(30, "30 minutes"), (120, "2 hrs"), (360, "6 hrs"), (1440, "1 day")],
    [],
]

DRONE_PRIVACY_LEVELS = [
    (0, 'NO privacy'), 
    (1, 'YES privacy')
]


####################################
# Used for the ICRAT survey version
####################################
VENDOR_TYPES_V_ICRAT = ['take-out food', '']
# Delivery fee
COST_LEVELS_V_ICRAT = [
    [0, 1, 3, 5],
    [],
]
# Delivery wait time in minutes
TIME_LEVELS_V_ICRAT = [
    [15, 20, 30, 45],
    [],
]
DRONE_PRIVACY_LEVELS_V_ICRAT = ['NO privacy', 'YES privacy']

