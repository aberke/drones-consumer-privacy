import csv
from string import Template

from attributes import (
    VENDOR_TYPES, COST_LEVELS, TIME_LEVELS, DRONE_PRIVACY_LEVELS
)


def generate_questions_block_txt(filepath):
    block_txt = ""
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        question = 0
        for row in reader:
            if not len(block_txt):
                block_txt = BLOCK_PREFIX_TEMPLATE.substitute(row)
            block_txt += generate_question_txt(row)
            question += 1
        print('generated %s questions' % question)
    return block_txt


def generate_question_txt(question_dict):
    v = int(question_dict['v'])
    question_dict.update({
        'v_value': VENDOR_TYPES[v],
        'gc_value': COST_LEVELS[v][int(question_dict['gc'])],
        'dc_value': COST_LEVELS[v][int(question_dict['dc'])],
        'gt_value': TIME_LEVELS[v][int(question_dict['gt'])],
        'dt_value': TIME_LEVELS[v][int(question_dict['dt'])],
        'dp_value': DRONE_PRIVACY_LEVELS[int(question_dict['dp'])]
    })
    return QUESTION_TEMPLATE.substitute(question_dict)

BLOCK_PREFIX_TEMPLATE = Template(
    """
    [[AdvancedFormat]]

    [[Block:v${v}]]
    """
)
QUESTION_TEMPLATE = Template(
    """

    [[Question:Matrix]]
    [[ID:CHOICE_v${v}_gc${gc}_gt${gt}_dc${dc}_dt${dt}_dp${dp}]]

    <style>
    .test-style {
        border: 1px solid red;
    }
    table.choices-table {
        width: 100%!important;
        border: 1px solid black;
        border-collapse: collapse!important;
        font-size: 0.9em;
    }
    table.choices-table tr td {
        padding: 1px;
        border-left: 1px solid black;
    }

    .choices-table td:nth-child(1) {
        width: 180px;
        text-align: left!important;
        padding-left: 3px;
    }
    .choices-table td:nth-child(2),
    .choices-table td:nth-child(3) {
        width: 270px;
    }

    .choices-table tr {
        border-bottom: 1px solid black;
    }
    .choices-table tr:first-child {
        border-bottom: none;
        font-weight: bold;
    }
    .choices-table tr:nth-child(2) {
        font-weight: bold;
    }
    .Skin label.QuestionText {
        padding-bottom: 5px!important;
    }
    .Skin .QuestionBody thead {
        display: table-footer-group;
    }

    </style>

    <p>Suppose you order ${v_value} for delivery to your home.</p>
    <p>Given the following delivery options, which <strong>one</strong> would you prefer?</p>

    <br/>
    <br/>

    <table class="choices-table">
    <tbody>
        <tr>
            <td>&nbsp;</td>
            <td>
                <img style="max-height:50px!important;" src="https://mit.co1.qualtrics.com/CP/Graphic.php?IM=IM_3rQUrJLUQ6syLmC" />
            </td>
            <td>
                <img style="max-height:50px!important;" src="https://mit.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_9XgV6C1HkKFFvM2" />
            </td>
        </tr>
        <tr>
            <td>Option</td>
            <td>Ground vehicle</td>
            <td>Drone</td>
        </tr>
        <tr>
            <td>Delivery fee</td>
            <td>$$${gc_value}</td>
            <td>$$${dc_value}</td>
        </tr>
        <tr>
            <td>Delivery wait time</td>
            <td>${gt_value} minutes</td>
            <td>${dt_value} minutes</td>
        </tr>
        <tr>
            <td>Privacy</td>
            <td>N/A</td>
            <td>${dp_value}</td>
        </tr>
    </tbody>
    </table>


    [[AdvancedChoices]]
    [[Choice]]
    <p>Preference</p>

    [[AdvancedAnswers]]
    [[Answer:0]]
    <p>Ground vehicle</p>

    [[Answer:1]]
    <p>Drone</p>
    """
)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
        Transform choice sets into Qualtrics Questions.
        Questions Block is saved to fpath.txt where fpath 
        is the filepath to the choice set csv.
        """)
    parser.add_argument('choiceset_fpath', metavar='f', type=str, nargs=1,
                    help='filepath for choice set csv (e.g. ./choice-sets/v1.csv)')
    
    args = parser.parse_args()
    csv_fpath = args.choiceset_fpath[0]
    block_txt = generate_questions_block_txt(csv_fpath)
    block_txt_fpath = csv_fpath + '.txt'
    print('writing questions block to file %s...' % block_txt_fpath)
    with open(block_txt_fpath, 'w') as block_txt_f:
        block_txt_f.write(block_txt)
    print('...done')
