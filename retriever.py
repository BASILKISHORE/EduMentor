def main(req):
    query = req.params.get('query')
    # Simulate retrieval from Blob Storage (replace with actual logic)
    return {'content': [f"Sample {query} resource"]}