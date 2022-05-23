# A simpkle implementation of the WhatsApp Cloud API with Flask

For this project, two functionaities were implemented:

- Sending messages.
- Receiving notifications via webhooks.

## Installation

Make sure to have an `.env` file with the following variables:

```shell
WHATSAPP_API_TOKEN=
WHATSAPP_NUMBER_ID=
WHATSAPP_NUMBER_WEBHOOK_TEST=
```

And install the dependencies:

```shell
pip install install -r requirements.txt
```

And then run the server:

```shell
flask run
```