dig-tokenizer
==================

Tokenizing documents based on configuration/rules


Requirements:
-------------
* Spark: Visit http://spark.apache.org/downloads.html, select the package type of “Pre-built for Hadoop 2.4 and later,” and then click on the link for “Download Spark” This will download a compressed TAR file, or tarball. Uncompress the file into ```<spark-folder>```.
Set SPARK_HOME PATH in bashrc.

Installation :
---------------
pip install digTokenizer


Running Tokenizer:
------------------

Format :

digTokenizer <options> <inputfile> <configfile> <outputpath>

outputpath is the folder created at the runtime. You need not create a folder.

Example Invocation:

With default options :

digTokenizer ~/github/datasets/sample-ad-location/sample.tsv ~/github/dig-tokenizer/sample_config.json \
    ~/github/datasets/sample-ad-location/tokens



Options Available for tokenizer utility :
   option name             description                         default value                          how to set
1. separator          delimiter to use between tokens      \t (use \n if required)             -r \n  or --separator \n
2. data-type         input file data type (csv/json)       csv (use json if required)          -d json or --type json
3. inputformat       is the input file text/sequence       text (use sequence if required)     -i sequence or --inputformat sequence
4. outputformat      is the output file text/sequence      text (use sequence if required)     -o sequence or --outputformat sequence



Sample Invocation :

digTokenizer --type json -o sequence newLSH_data/10k-ht_data-signs.jl newLSH_data/tokenizer.json tokens-body

description : as the input file is of type json lines and i need the output to be in sequence files i gave the options
--type json -o sequence and following arguments are input file, config file and output file.



Config file description :

Please have a look at the sample config file present in sample folder.
1. You can get tokens for multiple fields, if the input file is of type csv then it outputs tokens for all fields. You can custom at field level
the type of tokens you want. If you don't mention any analyzer for that field it will take defaultConfig values for that field.
2. Available options for tokenizers are whitespace, word_ngram and character_ngram. wordn_gram and character_ngram can
be defined for what value of n you want in settings.
3. There is an option for filters - which are lowercase, uppercase and latin. So if you use any of these filters will apply on respective fields
 and tokens are outputted.
4. prefix : if you want to add a prefix before every token for eg: if you are doing a tokenization of city and country fields, you want prefix of
'city' before every token. This option is the best deal for you.







**Recent changes to Tokenizer script :** <br />
<br />
1. Added a new filter called "mostlyHTML" - if the field contains mostly html tags then it will not output
any tokens - mostly html tags means i took a minimum of 40 tags, so if your field has more than 40 html tags
tokenizer won't output any tokens <br />
2. Added an extra feature for regex replacements in config file. Now you can add "word_replacements" in replacements
which are the regex expressions that will be applied on every word of field and "sent_replacements" which will be 
applied on the sentence level. Please check the config file 'unicode-tokenizer.json' for how to mention and sample files
to see the output.
