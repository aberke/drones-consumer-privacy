"""
Utility for importing into notebooks.
"""

# This is a dump from the recode values exported from qualtrics Q_state.
# Qualtrics put the states in alphabetical order for their recode value, did not code by FIPs
states_recode_text = '1\nAlabama\n2\nAlaska\n3\nArizona\n4\nArkansas\n5\nCalifornia\n6\nColorado\n7\nConnecticut\n8\nDelaware\n9\nDistrict of Columbia\n10\nFlorida\n11\nGeorgia\n12\nHawaii\n13\nIdaho\n14\nIllinois\n15\nIndiana\n16\nIowa\n17\nKansas\n18\nKentucky\n19\nLouisiana\n20\nMaine\n21\nMaryland\n22\nMassachusetts\n23\nMichigan\n24\nMinnesota\n25\nMississippi\n26\nMissouri\n27\nMontana\n28\nNebraska\n29\nNevada\n30\nNew Hampshire\n31\nNew Jersey\n32\nNew Mexico\n33\nNew York\n34\nNorth Carolina\n35\nNorth Dakota\n36\nOhio\n37\nOklahoma\n38\nOregon\n39\nPennsylvania\n40\nPuerto Rico\n41\nRhode Island\n42\nSouth Carolina\n43\nSouth Dakota\n44\nTennessee\n45\nTexas\n46\nUtah\n47\nVermont\n48\nVirginia\n49\nWashington\n50\nWest Virginia\n51\nWisconsin\n52\nWyoming\n53\nI do not reside in the United States'
states_recode_list = states_recode_text.split('\n')
states_choices_map = {states_recode_list[i]: states_recode_list[i+1] for i in range(0, len(states_recode_list), 2)}

# {QID: {Q: Q text, choices: map}}
codebook = {
    'Q_gender': {
        'Q':'What is your gender?',
        'choices': {'1':'Male','2':'Female','3':'Other', '4':'Prefer not to answer'},
    },
    'Q_age': {
        'Q': 'How old are you?',
        'choices': {
            '1':'18 - 24 years',
            '2':'25 - 34 years',
            '3':'35 - 44 years',
            '4':'45 - 54 years',
            '5':'55 - 64 years',
            '6':'65 or older'
        },
    },
    'Q_race': {
        'Q': 'Choose one or more races that you consider yourself to be',
        'choices': {
            '1':'White',
            '2':'Black or African American',
            '3':'American Indian or Alaska Native',
            '4':'Asian',
            '5':'Native Hawaiian or Pacific Islander',
            '6':'Hispanic or Latino',
            '7':'Other'
        },
    },
    'Q_income': {
        'Q': 'What was your total household income in the previous year before taxes?',
        'choices': {
            '1':'Less than \$25,000','2':'\$25,000 to \$49,999',
            '3':'\$50,000 to $74,999','4':'\$75,000 to \$99,999',
            '5':'\$100,000 to $149,999','6':'\$150,000 to \$199,999',
            '7':'\$200,000 or more',
        },
    },
    'Q_urban_rural': {
        'Q':'Which best describes where you live?',
        'choices': {'1':'Urban','2':'Suburban','3':'Rural','4':'I don\'t know'},
    },
    'Q_residence_type': {
        'Q':'What type of residence do you live in?',
        'choices': {'1':'Private home','2':'Apartment','3':'Other'},
    },
    'Q_state': {
        'Q':'In which state do you currently reside?',
        'choices': states_choices_map,
    },
    
    # would you ever order this for delivery?
    # not a v vendor
    'Q_online_shopping': {
        'Q': 'How often (on average) do you make online shopping purchases?',
        'choices': {
            '1':'More than once a week','2':'Multiple times a month',
            '3':'About once a month',
            '4':'Once in a few months or longer','5':'Never'
        }
    },
    # v0 - takeout food
    'Q_takeout_food': {
        'Q': 'How often (on average) do you have take-out food delivered to your home?',
        'choices': {
            '1':'More than once a week','2':'Multiple times a month',
            '3':'About once a month',
            '4':'Once in a few months or longer','5':'Never'
        }
    },
    # v1 - prescription medications
    'Q_v_1': {
        'Q': 'Suppose there is a company that specializes in delivering prescription medications and offers service in your area, and the total price is similar to local pharmacies. If you needed prescription medications, would you ever order them from this company for delivery to your home?',
        'choices': {
            '1':'Yes',
            '2':'No',
            '3':'I don\'t know'
        }
    },
    # v2 - liquor store
    'Q_v_2': {
        'Q': 'Would you ever order items from a liquor store for delivery to your home?',
        'choices': {
            '1':'Yes',
            '2':'No',
            '3':'I don\'t know'
        }
    },
    # v3
    'Q_online_groceries': {
        'Q': 'How often (on average) do you purchase your groceries online?',
        'choices': {
            '1':'More than once a week','2':'Multiple times a month',
            '3':'About once a month',
            '4':'Once in a few months or longer','5':'Never'
        }
    },
}
