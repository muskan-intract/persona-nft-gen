from db import db
from string import Template

def getPendingRecords(limit=10):
    personaNftCollection = db["tools.persona-nfts"]
    records = personaNftCollection.find({"status": "TX_CONFIRMED","imageGenerationStatus":"PUSHED_IN_QUEUE"}).sort("_id", 1).limit(limit)
    return records

def update_record_status(id,status):
    personaNftCollection = db["tools.persona-nfts"]
    personaNftCollection.update_one({"_id":id},{"$set":{"imageGenerationStatus":status}})
    return "Updated Successfully"

def substitute_template(html_template, metricsData, userAddress):
    template_without_value = Template(html_template)
    rendered_html = template_without_value.substitute(
        txncount=metricsData.get('txncount', '0'),
        gasPaid=metricsData.get('gasPaid', '$0'),
        uniqueAddressesInteractedWith=metricsData.get('uniqueAddressesInteractedWith', '0'),
        userAddress=userAddress,
        uniqueDaysActive=metricsData.get('uniqueDaysActive', '0d'),
        age=metricsData.get('age', '0d'),
        volume=metricsData.get('volume', '$0'),
        txncountPercentile=metricsData.get('txncountPercentile', '0%'),
        gasPaidPercentile=metricsData.get('gasPaidPercentile', '0%'),
        uniqueAddressesInteractedWithPercentile=metricsData.get('uniqueAddressesInteractedWithPercentile', '0%'),
        uniqueDaysActivePercentile=metricsData.get('uniqueDaysActivePercentile', '0%'),
        agePercentile=metricsData.get('agePercentile', '0%'),
        volumePercentile=metricsData.get('volumePercentile', '0%'),
    )
    return rendered_html