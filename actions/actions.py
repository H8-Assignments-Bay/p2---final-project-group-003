# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)


class ActionShowBalance(Action):
    """Shows the balance of account"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_show_balance"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        """Executes the custom action"""

        # show bank account balance
        account_balance = random.randint(1, 1000) * 50000
        # amount = tracker.get_slot("amount_transferred")
        dispatcher.utter_message(
            response="utter_account_balance",
            init_account_balance=f"{account_balance:,}",
        )

        events = []
        # active_form_name = tracker.active_form.get("name")
        # if active_form_name:
        #     # keep the tracker clean for the predictions with form switch stories
        #     events.append(UserUtteranceReverted())
        #     # trigger utter_ask_{form}_AA_CONTINUE_FORM, by making it the requested_slot
        #     events.append(SlotSet("AA_CONTINUE_FORM", None))
        #     # avoid that bot goes in listen mode after UserUtteranceReverted
        #     events.append(FollowupAction(active_form_name))

        return events
