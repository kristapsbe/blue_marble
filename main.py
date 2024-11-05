import json
import requests

from settings import username, password


base_url = "https://sh.dataspace.copernicus.eu/api/v1/process"

# https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Process/Examples/S2L2A.html
def get_token():
    return json.loads(
        requests.post(
            'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
            data = {
                'client_id': 'cdse-public',
                'username': username,
                'password': password,
                'grant_type': 'password'
            }
        ).content
    )['access_token']


evalscript = """
//VERSION=3
function setup() {
  return {
    input: [
      {
        bands: [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B11",
          "B12",
        ],
        units: "DN",
      },
    ],
    output: {
      id: "default",
      bands: 12,
      sampleType: SampleType.UINT16,
    },
  }
}

function evaluatePixel(sample) {
  return [
    sample.B01,
    sample.B02,
    sample.B03,
    sample.B04,
    sample.B05,
    sample.B06,
    sample.B07,
    sample.B08,
    sample.B8A,
    sample.B09,
    sample.B11,
    sample.B12,
  ]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            -94.04798984527588,
                            41.7930725281021,
                        ],
                        [
                            -94.04803276062012,
                            41.805773608962866,
                        ],
                        [
                            -94.06738758087158,
                            41.805901566741305,
                        ],
                        [
                            -94.06734466552734,
                            41.7967199475024,
                        ],
                        [
                            -94.06223773956299,
                            41.79144072064381,
                        ],
                        [
                            -94.0504789352417,
                            41.791376727347966,
                        ],
                        [
                            -94.05039310455322,
                            41.7930725281021,
                        ],
                        [
                            -94.04798984527588,
                            41.7930725281021,
                        ],
                    ]
                ],
            },
        },
        "data": [
            {
                "type": "sentinel-2-l2a",
                "dataFilter": {
                    "timeRange": {
                        "from": "2022-10-01T00:00:00Z",
                        "to": "2022-10-31T00:00:00Z",
                    }
                },
                "processing": {"harmonizeValues": "false"},
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {
                "identifier": "default",
                "format": {"type": "image/tiff"},
            }
        ],
    },
    "evalscript": evalscript,
}

print(get_token())

print(request)

quit()

response = requests.post(
    base_url,
    headers={"Authorization" : f"Bearer {get_token()}"},
    json=request
)

print(response)
print(response.headers)
#print(response.content)

with open(f'data/output_images.tar.gz', 'wb') as f:
    f.write(response.content)
