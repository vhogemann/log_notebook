# Receives an log message as the one bellow, and pretty-prints it with indentation and line breaks.:
# "Received authorisation request CardAuthorisationRequest{cardUid=e14ba927-05df-48d9-80e2-0ee64fcf3eed, authorisationRequest=AuthorisationRequest{systemsTraceAuditNumber=42541, messageId=MessageId{value='MC-20250618-MDH6FQTV1', settlementDate=2025-06-18, financialNetworkCode='MDH', bankNetRefNumber='6FQTV1'}, transmissionDateAndTime=2025-06-18T09:17:21Z, cardUid=e14ba927-05df-48d9-80e2-0ee64fcf3eed, merchantId=5960827        , acquirerInstitutionId=013908, transactionCode=PURCHASE, transactionCountry='826'}, pinValidationResult=NOT_PRESENT, trackValidationResult=TrackValidationResult{track1ValidationResult=NOT_PRESENT, track2ValidationResult=NOT_PRESENT, track2EquivalentValidationResult=NOT_PRESENT, cvc2ValidationResult=NOT_PRESENT, expiryDateValidationResult=VALID, cardExpiredValidationResult=VALID}, cryptogramValidationResult=NOT_PRESENT, authorisationUid=1bcd3965-5580-4310-b90c-89a98b6f18fd, cardholderVerificationMethod=CardholderVerificationMethod{continueIfUnsuccessful=true, methodCode=NO_CVM, conditionCode=NO_CVM, resultCode=NO_CVM}, mdesValidationResult=MDESValidationResult{panMapping=NOT_PRESENT, chipPrevalidation=NOT_PRESENT, cvc3Prevalidation=NOT_PRESENT, cloudChipPrevalidation=NOT_PRESENT, dynamicMagstripePrevalidation=NOT_PRESENT}, cryptogramInformationData=CryptogramInformationData{typeOfCryptogram=NOT_SET, adviceRequired='false', reasonCode='NOT_SET'}}, with DependentMessageId: MessageId{value='MC-20250618-MCC6FQRV1', settlementDate=2025-06-18, financialNetworkCode='MCC', bankNetRefNumber='6FQRV1'} transactionLink: null"
#  - Isolates CardAuthorisationRequest{ .. }
#  - Introduces line breaks and identation preseving the format

def format_card_authorisation_request(message: str) -> str:
    """
    Formats a card authorisation request message by isolating the CardAuthorisationRequest part,
    introducing line breaks and indentation while preserving the format.
    """
    # Isolate the CardAuthorisationRequest part
    start = message.find("CardAuthorisationRequest{")
    end = message.find("}", start) + 1
    request_part = message[start:end]

    # Introduce line breaks and indentation
    formatted_request = request_part.replace(", ", ",\n  ").replace("{", "{\n  ").replace("}", "\n}").replace("=", ": ")

    return formatted_request