# find files name in golden table
cat tac_kbp_2016_edl_evaluation_gold_standard_entity_mentions.tab | cut -d$'\t' -f 4 | cut -d ':' -f 1 |sort | uniq > /home/liang/internship/test/2016_gold_tab.txt

# find files name in document
ls source_documents/eng/nw/ > /home/liang/internship/test/2016_en_nw.txt


