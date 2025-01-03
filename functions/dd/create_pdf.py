import pdfrw
from pdfrw import PdfReader, PdfWriter

def fill_pdf(input_pdf, output_pdf, data_dict):
    template_pdf = PdfReader(input_pdf)

    for page in template_pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                field = annotation.get('/T')
                if field:
                    field_name = field[1:-1]  # Remove the surrounding parentheses
                    if field_name in data_dict:
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[field_name]))
                        )

    PdfWriter(output_pdf, trailer=template_pdf).write()

if __name__ == "__main__":
    input_pdf = '/Users/angela.romanovska/my-scripts/trading-calculator/functions/dd/pdf.pdf'
    output_pdf = 'filled_character_sheet.pdf'  # Path to save the filled PDF

    saving_throws = {
        'ST Strength': '2',
        'ST Charisma': '1',
        'ST Dexterity': '3',
        'ST Constitution': '4',
        'ST Intelligence': '2',
        'ST Wisdom': '5'
    }

    skills = {
        'Perception': '5',
        'Medicine': '3',
        'Performance': '4',
        'Acrobatics': '6',
        'Animal Handling': '7',
        'Arcana': '8',
        'Athletics': '9',
        'Deception': '4',
        'History': '3',
        'Insight': '6',
        'Intimidation': '2',
        'Investigation': '5',
        'Nature': '4',
        'Religion': '3',
        'Sleight of Hand': '7',
        'Stealth': '6',
        'Survival': '5'
    }

    main_throws = {
        'DEX': '14',
        'CHA': '12',
        'STR': '16',
        'CON': '13',
        'INT': '15',
        'WIS': '10'
    }

    extracted_fields = {
        'CharacterName': 'Angela',
        'Class': 'Wizard',
        'Race': 'Elf',
        'Background': 'Sage',
        'HitPoints': '30',
        'ArmorClass': '15',
        'Speed': '30'
    }

    common_list_of_fields = list(saving_throws.keys()) + list(skills.keys()) + list(main_throws.keys()) + list(extracted_fields.keys())

    data_dict = {}
    data_dict.update(saving_throws)
    data_dict.update(skills)
    data_dict.update(main_throws)
    data_dict.update(extracted_fields)

    fill_pdf(input_pdf, output_pdf, data_dict)
    print(f"Filled PDF saved as {output_pdf}")
