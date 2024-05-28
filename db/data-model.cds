namespace my.bookshop;

entity Books {
  key ID : Integer;
  title  : String;
  stock  : Integer;
}

entity Telecom_Churn{
  key phone_number         : Integer;
    international_plan       : Integer;
    voice_mail_plan          : Integer;
    number_vmail_messages    : Integer;
    total_day_minutes        : Decimal(5,2);
    total_day_calls          : Integer;
    total_day_charge         : Decimal(5,2);
    total_eve_minutes        : Decimal(5,2);
    total_eve_calls          : Integer;
    total_eve_charge         : Decimal(5,2);
    total_night_minutes      : Decimal(5,2);
    total_night_calls        : Integer;
    total_night_charge       : Decimal(5,2);
    total_intl_minutes       : Decimal(4,2);
    total_intl_calls         : Integer;
    total_intl_charge        : Decimal(4,2);
    customer_service_calls   : Integer;
    churn                    : Integer;
}


entity InsuranceData {
    
    age    : Integer;
    sex    : String(6);    // Can be "male" or "female"
    bmi    : Decimal(5,3);
    children : Integer;
    smoker : String(3);    // Can be "yes" or "no"
    region : String(100);  // Assuming region names are less than 100 characters
    charges : Integer
}

