const cds = require('@sap/cds');
const axios = require('axios');
const cfenv = require('cfenv')



module.exports = cds.service.impl(async function () {
    const { InsuranceData } = this.entities;

    this.on('READ', InsuranceData, async (req) => {
        try {
            // Fetch data from the database
            const insuranceData = await cds.tx(req).run(
                SELECT.from(InsuranceData)
            );

            // Log the first record for debugging
            console.log(insuranceData[0]);

            // Make the POST request to the external API
            const response = await axios.post('https://insurance-unexpected-turtle-zt.cfapps.us10-001.hana.ondemand.com/getPrice', insuranceData)

            // Log the response for debugging
            console.log(response);
            // 
            // to get the hana db details
            const DESTINATION_SERVICE = cfenv.getAppEnv().services.hana
            console.log(DESTINATION_SERVICE)

            // Return the response from the external API
            return  insuranceData;
        } catch (err) {
            // Log the error for debugging
            console.error(err);

            // Return a proper error message
            req.error(500, 'Error fetching data from the database or calling external API');
        }
    });
});


















