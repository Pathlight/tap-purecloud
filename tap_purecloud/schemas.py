historical_adherence = {
    'type': 'object',
    'properties': {
        "userId": {
            "type": ["null", "string"]
        },
        "startDate": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "endDate": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "impact": {
            "type": ["null", "string"]
        },
        "exceptionInfo": {
            "type": ["null", "array"],
            "items": {
                "type": ["object", "null"]
            }
        },
        "management_unit_id": {
            "type": ["null", "string"]
        },
        "dayMetrics": {
            "type": ["null", "array"],
            "items": {
                "type": ["null", "object"],
                "properties": {
                    "dayStartOffsetSecs": {
                        "type": ["null", "number"]
                    },
                    "adherenceScheduleSecs": {
                        "type": ["null", "number"]
                    },
                    "conformanceScheduleSecs": {
                        "type": ["null", "number"]
                    },
                    "conformanceActualSecs": {
                        "type": ["null", "number"]
                    },
                    "exceptionCount": {
                        "type": ["null", "number"]
                    },
                    "exceptionDurationSecs": {
                        "type": ["null", "number"]
                    },
                    "impactSeconds": {
                        "type": ["null", "number"]
                    },
                    "scheduleLengthSecs": {
                        "type": ["null", "number"]
                    },
                    "actualLengthSecs": {
                        "type": ["null", "number"]
                    }
                }
            }
        }
    }
}

users = {
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "division": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "self_uri": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "self_uri"
      ]
    },
    "chat": {
      "type": "object",
      "properties": {
        "jabber_id": {
          "type": "string"
        }
      },
      "required": [
        "jabber_id"
      ]
    },
    "department": {
      "type": [
        "null",
        "string"
      ]
    },
    "email": {
      "type": "string"
    },
    "primary_contact_info": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "address": {
            "type": "string"
          },
          "display": {
            "type": [
              "null",
              "string"
            ]
          },
          "media_type": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "extension": {
            "type": "null"
          },
          "country_code": {
            "type": "null"
          },
          "integration": {
            "type": "null"
          }
        },
        "required": [
          "address",
          "country_code",
          "display",
          "extension",
          "integration",
          "media_type",
          "type"
        ]
      }
    },
    "addresses": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "address": {
            "type": "string"
          },
          "display": {
            "type": [
              "null",
              "string"
            ]
          },
          "media_type": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "extension": {
            "type": "null"
          },
          "country_code": {
            "type": [
              "null",
              "string"
            ]
          },
          "integration": {
            "type": "null"
          }
        },
        "required": [
          "address",
          "country_code",
          "display",
          "extension",
          "integration",
          "media_type",
          "type"
        ]
      }
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": [
        "null",
        "string"
      ]
    },
    "username": {
      "type": "string"
    },
    "manager": {
      "type": "null"
    },
    "images": {
      "anyOf": [
        {
          "type": "null"
        },
        {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "resolution": {
                "type": "string"
              },
              "image_uri": {
                "type": "string"
              }
            },
            "required": [
              "image_uri",
              "resolution"
            ]
          }
        }
      ]
    },
    "version": {
      "type": "integer"
    },
    "certifications": {
      "type": "null"
    },
    "biography": {
      "type": "null"
    },
    "employer_info": {
      "type": "null"
    },
    "routing_status": {
      "type": "null"
    },
    "presence": {
      "type": "null"
    },
    "integration_presence": {
      "type": "null"
    },
    "conversation_summary": {
      "type": "null"
    },
    "out_of_office": {
      "type": "null"
    },
    "geolocation": {
      "type": "null"
    },
    "station": {
      "type": "null"
    },
    "authorization": {
      "type": "null"
    },
    "profile_skills": {
      "type": "null"
    },
    "locations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "null"
          },
          "floorplan_id": {
            "type": "null"
          },
          "coordinates": {
            "type": [
              "null",
              "object"
            ]
          },
          "notes": {
            "type": "string"
          },
          "location_definition": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "name": {
                "type": "null"
              },
              "contact_user": {
                "type": "null"
              },
              "emergency_number": {
                "type": "null"
              },
              "address": {
                "type": "null"
              },
              "state": {
                "type": "null"
              },
              "notes": {
                "type": "null"
              },
              "version": {
                "type": "null"
              },
              "path": {
                "type": "null"
              },
              "profile_image": {
                "type": "null"
              },
              "floorplan_image": {
                "type": "null"
              },
              "address_verification_details": {
                "type": "null"
              },
              "address_verified": {
                "type": "null"
              },
              "address_stored": {
                "type": "null"
              },
              "images": {
                "type": "null"
              },
              "self_uri": {
                "type": "string"
              }
            },
            "required": [
              "address",
              "address_stored",
              "address_verification_details",
              "address_verified",
              "contact_user",
              "emergency_number",
              "floorplan_image",
              "id",
              "images",
              "name",
              "notes",
              "path",
              "profile_image",
              "self_uri",
              "state",
              "version"
            ]
          }
        },
        "required": [
          "coordinates",
          "floorplan_id",
          "id",
          "location_definition",
          "notes"
        ]
      }
    },
    "groups": {
      "type": "null"
    },
    "team": {
      "type": "null"
    },
    "skills": {
      "type": "null"
    },
    "languages": {
      "type": "null"
    },
    "acd_auto_answer": {
      "type": "boolean"
    },
    "language_preference": {
      "type": "null"
    },
    "last_token_issued": {
      "type": "null"
    },
    "date_last_login": {
      "type": "null"
    },
    "self_uri": {
      "type": "string"
    }
  },
  "required": [
    "acd_auto_answer",
    "addresses",
    "authorization",
    "biography",
    "certifications",
    "chat",
    "conversation_summary",
    "date_last_login",
    "department",
    "division",
    "email",
    "employer_info",
    "geolocation",
    "groups",
    "id",
    "images",
    "integration_presence",
    "language_preference",
    "languages",
    "last_token_issued",
    "locations",
    "manager",
    "name",
    "out_of_office",
    "presence",
    "primary_contact_info",
    "profile_skills",
    "routing_status",
    "self_uri",
    "skills",
    "state",
    "station",
    "team",
    "title",
    "username",
    "version"
  ]
}

group = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'description': 'name for the group',
        },
        'id': {
            'type': 'string',
            'description': 'id for the group',
        },
        'state': {
            'type': 'string',
            'description': 'state for the group',
        },
        'visibility': {
            'type': 'string',
            'description': 'visibility for the group',
        }
    }
}

location = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the location',
        },
        'name': {
            'type': 'string',
            'description': 'name for the location',
        },
        'state': {
            'type': 'string',
            'description': 'state for the location',
        }
    }
}


conversation = {
    'type': 'object',
    'properties': {
        'conversation_id': {
            'type': 'string',
            'description': 'id for the conversation',
        },
        'conversation_start': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'start timestamp for the conversation',
        },
        'conversation_end': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'end timestamp for the conversation',
        },
        "division_ids": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "conversation_initiator": {
            "type": ["string", "null"]
        },
        "media_stats_min_conversation_mos": {
            "type": ["number", "null"]
        },
        "media_stats_min_conversation_r_factor": {
            "type": ["number", "null"]
        },
        "originating_direction": {
            "type": ["string", "null"]
        },
        "customer_participation": {
            "type": ["boolean", "null"]
        },
    }
}

conversation_participant = {
   'type': 'object', 
   'properties': {
        'conversation_id': {
            'type': 'string',
            'description': 'id for the conversation'
        },
        'participant_id': {
            'type': 'string',
            'description': 'id for the participant'
        },
        'participant_name': {
            'type': ['string', 'null'],
            'description': 'name for the participant'
        },
        "user_id": {
            "type": ["string", "null"]
        },
        "flagged_reason": {
            "type": ["string", "null"]
        },
        "purpose": {
            "type": ["string", "null"]
        },
   }
}

conversation_participant_session = {
    'type': 'object', 
    'properties': {
        'conversation_id': {
            'type': 'string',
            'description': 'id for the conversation'
        },
        'participant_id': {
            'type': 'string',
            'description': 'id for the participant'
        },
        'session_id': {
            'type': 'string',
            'description': 'id for the session'
        },
        'direction': {
            'type': 'string'
        },
        "acw_skipped": {
            "type": ["boolean", "null"]
        },
        "assigner_id": {
            "type": ["string", "null"]
        },
        "media_type": {
            "type": ["string", "null"]
        },
        "message_type": {
            "type": ["string", "null"]
        },
        "outbound_campaign_id": {
            "type": ["string", "null"]
        },
        "provider": {
            "type": ["string", "null"]
        },
        "recording": {
            "type": ["boolean", "null"]
        },
        "selected_agent_id": {
            "type": ["string", "null"]
        }
    }
}

conversation_participant_session_segment = {
    "type": "object",
    "properties": {
        "conversation_id": {
            "type": "string",
            "description": "id for the conversation"
        },
        "destination_conversation_id": {
            "type": ["string", "null"]
        },
        "participant_id": {
            "type": "string",
            "description": "id for the participant"
        },
        "session_id": {
            "type": "string",
            "description": "id for the session"
        },
        "destination_session_id": {
            "type": ["string", "null"]
        },
        "segment_start": {
            "type": "string",
            "format": "date-time",
            "description": "start datetime for the segment"
        },
        "segment_end": {
            "type": ["string", "null"],
            "format": "date-time",
            "description": "end datetime for the segment"
        },
        "segment_type": {
            "type": "string"
        },
        "queue_id": {
            "type": ["string", "null"]
        },
        "group_id": {
            "type": ["string", "null"]
        },
        "subject": {
            "type": ["string", "null"]
        },
        "source_conversation_id": {
            "type": ["string", "null"]
        },
        "source_session_id": {
            "type": ["string", "null"]
        }
    }
}

conversation_participant_session_metric = {
    "type": "object",
    "properties": {
        "conversation_id": {
            "type": "string",
            "description": "id for the conversation"
        },
        "participant_id": {
            "type": "string",
            "description": "id for the participant"
        },
        "session_id": {
            "type": "string",
            "description": "id for the session"
        },
        "name": {
            "type": "string"
        },
        "value": {
            "type": "number"
        },
        "emit_date": {
            "type": "string",
            "format": "date-time"
        }
    }
}


user_state = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the user state',
        },
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        },
        'start_time': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'start time',
        },
        'end_time': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'end time',
        },
        'state': {
            'type': 'string',
            'description': 'state'
        },
        'state_id': {
            'type': ['string', 'null'],
            'description': 'state id'
        },
        'type': {
            'type': 'string',
            'description': 'message type'
        }
    }
}

management_unit = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the management unit',
        },
        'name': {
            'type': 'string',
            'description': 'name for the management unit',
        }
    }
}

activity_code = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the activity code',
        },
        'management_unit_id': {
            'type': 'string',
            'description': 'id for the management unit for this activity code',
        },
        'name': {
            'type': 'string',
            'description': 'name for this activity code',
        },
        'category': {
            'type': 'string',
            'description': 'category for this activity code',
        }
    }
}

management_unit_users = {
    'type': 'object',
    'properties': {
        'management_unit_id': {
            'type': 'string',
            'description': 'id for the management unit for this user',
        },
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        }
    }
}

user_schedule = {
    'type': 'object',
    'properties': {
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        },
        'start_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'date for the sync',
        },
        "metadata": {
            "type": ["object", "null"],
            "properties": {
                "version": {
                    "type": "number"
                },
                "modified_by": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                    }
                },
                "date_modified": {
                    "type": "string",
                    "format": "date-time"
                },
                "created_by": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                    }
                },
                "date_created": {
                    "type": "string",
                    "format": "date-time"
                }
            }
        },
        "work_plan_id": {
            "type": ["string", "null"]
        }
    }
}

user_schedule_shift = {
    'type': 'object',
    'properties': {
        "id": {
            "type": "string"
        },
        "user_id": {
            "type": "string"
        },
        "length_in_minutes": {
            "type": "number"
        },
        "week_schedule": {
            "type": "object",
            "description": "The schedule to which this shift belongs",
            "properties": {
                "id": {
                    "type": "string"
                },
                "week_date": {
                    "type": "string"
                }
            }
        },
        'start_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'date for the shift',
        },
        "delete": {
            "type": ["boolean", "null"]
        },
        "manually_edited": {
            "type": ["boolean", "null"]
        }
    }
}

user_schedule_shift_activity = {
    'type': 'object',
    'properties': {
        "user_id": {
            "type": "string"
        },
        "shift_id": {
            "type": "string"
        },
        "week_schedule_id": {
            "type": "string"
        },
        'activity_code_id': {
            'type': 'string',
            'description': 'id for the activity_code',
        },
        "start_date": {
            "type": "string",
            "format": "date-time",
        },
        "length_in_minutes": {
            "type": "number"
        },
        "description": {
            "type": "string"
        },
        "counts_as_paid_time": {
            "type": "boolean"
        },
        "is_dst_fallback": {
            "type": ["boolean", "null"]
        },
        "time_off_request_id": {
            "type": ["string", "null"]
        }

    }
}

presence_label = {
    'type': 'object',
    'properties': {
        'en_US': {
            'type': 'string',
            'description': 'English presence label'
        }
    }
}

presence = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'presence id',
        },
        'language_labels': presence_label,
        'created_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'presence creation date',
        },
        'modified_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'presence modification date',
        }
    }
}

queue = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'queue id',
        },
        'name': {
            'type': 'string',
            'name': 'queue name',
        },
        'member_count': {
            'type': 'number',
            'name': 'queue member count',
        },
        'created_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'queue creation date',
        },
        'modified_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'queue modification date',
        }
    }
}

queue_membership = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'id for the user membership in this queue',
        },
        'queue_id': {
            'type': 'string',
            'name': 'id for the queue',
        },
        'user_id': {
            'type': 'string',
            'name': 'user id for this queue',
        }
    }
}

queue_wrapup = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'id for the wrapup code in this queue',
        },
    }
}
