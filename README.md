# ScribDl

A simple script to download image-based Scribd documents. Downloads consecutively according to the HTML element ordering.

## Installation

Simply download `scribDl.py`.
In your command line, type:
```pip install requests```

## Usage

Navigate to the Scribd document webpage. Right click on the document in the browser and hit "inspect" (may be different per browser). The element should be a div with class `document_container`. Copy the entire HTML element and save it into a file.

Run the following command in your terminal window:
```
python scribDl.py [div_element_filename] [folder_to_save_images]
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.
