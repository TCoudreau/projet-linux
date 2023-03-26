doge=$(curl -s https://crypto.com/price/fr/dogecoin | grep -oP '(?<=<span class="chakra-text css-13hqrwd">\$)[\d.]+(?= USD</span>)')
datetime=$(date +'%F %T')
value="$datetime,$doge"
echo $value >> history.csv