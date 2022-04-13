# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import logging
import json
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction, FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)

USER_INTENT_OUT_OF_SCOPE = "out_of_scope"

logger = logging.getLogger(__name__)

"""_summary_
    Update the Slot Value of Input1 to None
Returns:
    Slot to None
"""
 
"""_summary_
    Update the Slot Value of Input5 to None
Returns:
    Slot to None
"""
class ActionSetInput1(Action):

    def name(self) -> Text:
        return "action_set_input1_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input1", None)]
     
class ActionSetInput3(Action):
    
    def name(self) -> Text:
        return "action_set_input3_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input3", None)] 
 
    
class ActionSetInput5(Action):
    
    def name(self) -> Text:
        return "action_set_input5_slot_none"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("input5", None)]   

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_input0_1_2_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_intent = tracker.latest_message['intent'].get('name')
        print(last_intent)
        input0_slot = tracker.get_slot("input0")
        if input0_slot:
            print("input1_slot",input0_slot)
        #     dispatcher.utter_message(template="utter_input3_0")
        input1_slot = tracker.get_slot("input1")
        if input1_slot:
            print("input1_slot",input1_slot)
            dispatcher.utter_message(template="utter_input3_1")
        else:
            dispatcher.utter_message(template="utter_input3_0")
        return []        
