{
  "name": "Daily Report Bot",
  "nodes": [
    {
      "parameters": {
        "formTitle": "Ahamed's Daily Progress Report",
        "formDescription": "Submit your daily learning activities, project progress,\nchallenges and plans for tomorrow.",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Raihan"
            },
            {
              "fieldLabel": "Today's Learning",
              "fieldType": "textarea"
            },
            {
              "fieldLabel": "Project Work Completed",
              "fieldType": "textarea"
            },
            {
              "fieldLabel": "Time Spent (Hours)",
              "fieldType": "number"
            },
            {
              "fieldLabel": "Challenges Faced",
              "fieldType": "textarea"
            },
            {
              "fieldLabel": "Tomorrow's Plan",
              "fieldType": "textarea"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.6,
      "position": [
        0,
        0
      ],
      "id": "7a05d883-dac3-41f5-a9f0-7a2d61825c29",
      "name": "On form submission",
      "webhookId": "802a6b14-ebf1-4448-9916-2b657c12268a"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "bdc21d7e-e057-4e0b-8aff-c51dc12fa8a9",
              "name": "daily_report",
              "value": "={{\n\"📊 DAILY PROGRESS REPORT\\n\\n\" +\n\"Name: \" + $json[\"Raihan\"] + \"\\n\" +\n\"Date: \" + $json[\"submittedAt\"] + \"\\n\\n\" +\n\"📚 Today's Learning:\\n\" +\n$json[\"Today's Learning\"] + \"\\n\\n\" +\n\"💻 Project Work:\\n\" +\n$json[\"Project Work Completed\"] + \"\\n\\n\" +\n\"⏰ Time Spent: \" +\n$json[\"Time Spent (Hours)\"] + \" hours\\n\\n\" +\n\"⚠️ Challenges:\\n\" +\n$json[\"Challenges Faced\"] + \"\\n\\n\" +\n\"🎯 Tomorrow's Plan:\\n\" +\n$json[\"Tomorrow's Plan\"]\n}}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.5,
      "position": [
        224,
        0
      ],
      "id": "3af5d0d8-0db5-4d2b-8235-4049d79e4399",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "fromEmail": "i.ahamedraihan@gmail.com",
        "toEmail": "i.ahamedraihan@gmail.com",
        "subject": "Daily Progress Report",
        "emailFormat": "text",
        "text": "={{ $json.daily_report }}",
        "options": {}
      },
      "type": "n8n-nodes-base.emailSend",
      "typeVersion": 2.1,
      "position": [
        448,
        0
      ],
      "id": "69fb1adb-a249-4760-95a0-b58ee0f4839f",
      "name": "Send an Email",
      "webhookId": "8de5ef9b-0b5c-4e10-9200-4971ccc57892",
      "credentials": {
        "smtp": {
          "id": "pYRB4vBQ7vCSBGWP",
          "name": "SMTP account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "On form submission": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Send an Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1",
    "binaryMode": "separate"
  },
  "versionId": "f5f93a11-2869-4729-9ff2-f3d2044fd050",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "d3ed8b73bd7515c31c999c68921d7ca8c9f26b21742dabf9e3e0cbb547bc1969"
  },
  "nodeGroups": [],
  "id": "kDpQTozLBZt3cfNf",
  "tags": []
}