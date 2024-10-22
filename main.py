import os
import requests


token = os.getenv("ACCESS_TOKEN")
base_url = "https://sh.dataspace.copernicus.eu/api/v1/process"


# https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Process/Examples/S2L2A.html
evalscript = """
//VERSION=3
function setup() {
    return {
        input: ["B02", "B03", "B04"],
        output: {
            bands: 3,
            sampleType: "AUTO", // default value - scales the output values from [0,1] to [0,255].
        },
    }
}

function evaluatePixel(sample) {
    return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
            "bbox": [
                23.5,
                56.5,
                24.5,
                57.5,
            ],
        },
        "data": [
            {
                "type": "sentinel-2-l2a",
                "dataFilter": {
                    "timeRange": {
                        "from": "2022-06-01T00:00:00Z",
                        "to": "2022-06-30T00:00:00Z",
                    }
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
    },
    "evalscript": evalscript,
}

response = requests.post(
    base_url,
    headers={"Authorization" : f"Bearer {token}"},
    json=request
)

if response.status_code == 200:
    with open('output_image.png', 'wb') as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code} - {response.text}")
