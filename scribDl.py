import sys, os
import re
import urllib.request, requests

FOLDER_NAME = 'Assets'

def grab_asset(line, output_list=None):
  asset = None
  if line.strip().startswith('<img'):
    # Grab the image URL from the img tag.
    asset = re.search('"(?P<url>https?://[^\s]+)"', line).group('url')
  if line.strip().startswith('pageParams.contentUrl'):
    # Grab the script URL from script line.
    script_url = re.search('"(?P<url>https?://[^\s]+)"', line).group('url')

    # Grab the image URL from the script file.
    get_body = requests.get(script_url).text
    asset = re.search('"(?P<url>https?://[^\s]+)\\\\"', get_body).group('url')
  
  if output_list is not None:
    if asset is not None:
      output_list.append(asset)
  return asset

def file_to_assets(fname):
  assets = []
  with open(fname) as f:
    for line in f:
      grab_asset(line, assets)
  return assets

def save_assets_to_folder(assets, folder_name=FOLDER_NAME):
  for i, img_link in enumerate(assets):
    ext = img_link.split('.')[-1]
    urllib.request.urlretrieve(img_link, '%s/%d.%s' % (folder_name, i + 1, ext))

def main(argv):
  # File name must be specified.
  if len(argv) < 1:
    print('No div file specified.')
    sys.exit(0)
  # Folder name is optional.
  folder_name = FOLDER_NAME
  if len(argv) > 1:
    folder_name = argv[1]

  fname = argv[0]
  assets = file_to_assets(fname)
  print('Scanned file and found %d images.' % len(assets))

  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
  save_assets_to_folder(assets, folder_name)
  print('Finished! Completely downloaded %d images and saved to %s.' % (len(assets), folder_name))

if __name__ == "__main__":
  main(sys.argv[1:])
