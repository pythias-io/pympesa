M-PESA API | Python Client
==========================

Mpesa Rest API python library implementing the following endpoints:

  * Lipa na mpesa online
  * B2B
  * B2C
  * C2B
  * Transaction status
  * Account balance
  * Reversal


Getting Started
---------------
Installation:

.. code-block:: bash

    pip install pympesa

Set up your environment by exporting the variables on `pympesa.env.tmpl`

Usage:

  1. Create your app on https://developer.safaricom.co.ke/user/me/apps  [+ Add a new App]
  2. Your app will be created with a <CONSUMER_KEY> and a <CONSUMER_SECRET>
  3. Generate a time bound oauth access token which will enable you to call this APIs.

.. code-block:: python
     
    import pympesa

    response = pympesa.oauth_generate_token(
        consumer_key, consumer_secret).json()
    access_token = response.get("access_token")

  4. With this access token you can now call the APIs.
  
Register your callback URLs

.. code-block:: python

    from pympesa import Pympesa

    mpesa_client = Pympesa(access_token)
    mpesa_client.c2b_register_url(
        ValidationUrl="https://your-app/validate",
        ConfirmationUrl="https://your-app/confirm",
        ResponseType="Completed",
        ShortCode="01234"
        )

Initiate Lipa na M-PESA online (triggering STK Push)

.. code-block:: python

    mpesa_client.lipa_na_mpesa_online_payment(
        BusinessShortCode="600000",
        Password="xxxxx_yyyy_zzz",
        TransactionType="CustomerPayBillOnline",
        Amount="100",
        PartyA="254708374149",
        PartyB="600000",
        PhoneNumber="254708374149",
        CallBackURL="https://your-app/callback",
        AccountReference="ref-001",
        TransactionDesc="desc-001"
        )



Changelog
---------

0.3 - 2017/09/19
~~~~~~~~~~~~~~~~

- Initial version

0.4 - 2017/10/19
~~~~~~~~~~~~~~~~

- Added testcases
