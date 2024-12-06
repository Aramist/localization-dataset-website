source /mnt/home/atanelus/.bashrc
source /mnt/home/atanelus/venvs/general/bin/activate

python scripts/generate_html.py \
    --strings /mnt/home/atanelus/dataset_website/scripts/strings \
    --templates /mnt/home/atanelus/dataset_website/scripts/templates \
    -o /mnt/home/atanelus/dataset_website/src/index.html
echo "Publishing to public_www..."
rsync -a --delete --no-links src/ /mnt/home/atanelus/public_www/
echo "Done."

echo "Symlinking download links..."
python scripts/make_download_links.py
echo "Done."