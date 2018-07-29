# scrapy all the html document
wget -r -np -nH –cut-dirs=3 -R “index.html*” https://blender04.cs.rpi.edu/~panx2/tmp/typing/


# delete all the index*.html files
find . -name "index*" -type f -delete 





# the code for checking the nested mention, need to use Sublime to show. 
grep ENG_NW_001278_20130113_F00013PQC tac_kbp_2017_edl_evaluation_gold_standard_entity_mentions.tab | awk 'BEGIN { FS="\t"} {print $4}'| cut -d ':' -f 2 | awk '$1=$1' ORS=','

#Sort
awk 'BEGIN { FS="\t"} {print $3,$4}' test.tab |column -t -s $'\t' | sort -t: -k2 -g

's/ENG_DF_001471_20060203_G00A0275Q:/ /' sorted_ENG_DF_001471_20060203_G00A0275Q.txt 

#Show the nested mention 
cut -d$'\t' -f4 tac_kbp_2017_edl_evaluation_gold_standard_entity_mentions.tab | cut -d '-' -f 1 | sort  |uniq -c| grep -v '^ *1 '|sort


#find the code for subline region selecting in region_select.py
