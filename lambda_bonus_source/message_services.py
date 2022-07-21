import copy

template = {
    "color": "#008000",
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                # change!
                "text": None
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Description:*\n"
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Edit"
                    },
                    "action_id": "bonus_edit_"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Delete"
                    },
                    "style": "danger",
                    "action_id": "bonus_delete_"
                }
            ]
        }
    ]
}


def get_bonus_by_id(bonus_id, bonus_list):
    for bonus in bonus_list:
        if bonus['id'] == bonus_id:
            return bonus

    return None


def generate_bonus_block_list(bonus_list, template=template):
    attachments = []

    for bonus in bonus_list:
        temp = copy.deepcopy(template)
        temp['blocks'][0]['text']['text'] = bonus['name']
        temp['blocks'][1]['fields'][0]['text'] += bonus['description']
        temp['blocks'][2]['elements'][0]['action_id'] += str(bonus['id'])
        temp['blocks'][2]['elements'][1]['action_id'] += str(bonus['id'])

        attachments.append(temp)

    attachments.append(back_to_bonus_start_menu_button)

    return attachments


bonus_edited_successfully = {
    "type": "section",
    "text": {
        "type": "plain_text",
        "text": "Bonus was edited successfully"
    }
}


def bonus_created_successfully(name):
    return {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": f"Bonus {name} was created successfully"
        }
    }


bonus_start_menu = [
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Bonus List"
                },
                "action_id": "bonus_list"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Create bonus"
                },
                "action_id": "bonus_create"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Return to main menu"
                },
                "action_id": "start_menu"
            }
        ]
    }
]

back_to_bonus_start_menu_button = {
    "color": "#008000",
    "blocks": [
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Back"
                    },
                    "action_id": "bonus_start_menu"
                }
            ]
        }
    ]
}

bonus_create_modal = {
    "title": {
        "type": "plain_text",
        "text": "Create new bonus"
    },
    "submit": {
        "type": "plain_text",
        "text": "Create"

    },
    "type": "modal",
    "callback_id": "bonus_modal_create",
    "close": {
        "type": "plain_text",
        "text": "Cancel"
    },
    "blocks": [
        {
            "type": "input",
            "label": {
                "type": "plain_text",
                "text": "Bonus name"
            },
            "element": {
                "type": "plain_text_input",
                "action_id": "bonus_name_input"
            },
        },
        {
            "type": "input",
            "label": {
                "type": "plain_text",
                "text": "Description"
            },
            "element": {
                "type": "plain_text_input",
                "action_id": "bonus_description_input",
                "multiline": True
            }
        }
    ]
}


def bonus_edit_modal(bonus_id, name, description):
    return {
        "title": {
            "type": "plain_text",
            "text": "Edit bonus"
        },
        "submit": {
            "type": "plain_text",
            "text": "Save"

        },
        "type": "modal",
        "callback_id": "bonus_modal_edit_" + str(bonus_id),
        "close": {
            "type": "plain_text",
            "text": "Cancel"
        },
        "blocks": [
            {
                "type": "input",
                "label": {
                    "type": "plain_text",
                    "text": "Bonus name"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "bonus_name_input",
                    "initial_value": name
                },
            },
            {
                "type": "input",
                "label": {
                    "type": "plain_text",
                    "text": "Description"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "bonus_description_input",
                    "initial_value": description,
                    "multiline": True
                }
            }
        ]
    }