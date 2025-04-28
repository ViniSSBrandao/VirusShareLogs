This repository is being used to store the logs of the filetype signatures of each individual archive present in the virusshare files. <br/>
You can check how many files of each type are available in each Virus Share pack by checking the TypeCounts folder and opening the ./TypeCounts/mime_counts00xyz.csv (which corresponds to the virushare pack number) that contains that counting. If you want to get the individual hashes for the filetype you are looking for, check the Logs_By_VirusShare folder and then open the corresponding folder containing the same pack number as the one desired. <br/>

None of the VirusShare files will be available here for security reasons. If you are interested in checking their catalog, check out their website https://virusshare.com/

## available tools

## Count Aggregation `log_classification_and_separation.py`



🚀 Features

- Load data: Reads the specified CSV files containing hash records and MIME types.
- Count MIME type occurrences: Aggregates the number of occurrences for each MIME type.
- Save MIME counts: Exports the MIME type count data to a CSV file.


Group and save records by MIME type: Organizes and saves separate CSV files containing records of each MIME type.

Print summary: Displays the MIME type count DataFrame.

📥 Requisites & How to use:

Python 3.x with pandas library installed is required

CSV files structured with a MIME_type column (on the path set on the file)

Set the block variable to specify the VirusShare package (or other pool of files) being processed.

Ensure the source CSV file exists at Untreated_logs/registro_destino_<block>.csv. (or personalize this to your particular use)

Run the script using your python interpreter to generate categorized logs and a summary CSV file.

📂 Expected Outputs

TypeCounts/mime_counts<block>.csv: Contains a count of each MIME type.

Separate CSV files in Logs_By_VirusShare/<block>/ categorized by MIME type.

Example Output:
        TypeCounts/Mime_counts004xx.csv: (will contain the counts for statistical analysis)

           MIME_type          Count  Virus_Share_Package
        application/pdf    150    Untreated_logs/registro_destino_00478.csv
        text/html          100    Untreated_logs/registro_destino_00478.csv
        ...
<br/>
        Logs_by_VirusShare/004xx/mime_type1.csv (each will contain the hashes for the files for reference and verification)<br/>
        Logs_by_VirusShare/004xx/mime_type2.csv  <br/>
        Logs_by_VirusShare/004xx/mime_type3.csv:

           MIME_type                                    Count               Virus_Share_Package
          VirusShare_c6f2507196ec200d4dcca46898ce09f9	application/gzip	./sample_classification/application_gzip
          VirusShare_0f41ed97b32463ec0eee297496bf7cf3	application/gzip	./sample_classification/application_gzip
          VirusShare_43e5f4995f11aea446fe54355cfd8ab9	application/gzip	./sample_classification/application_gzip
          VirusShare_0ee7f4ff292de45c1f733d994661345e	application/gzip	./sample_classification/application_gzip
          VirusShare_e153bacb64b4b635cca2538198b87459	application/gzip	./sample_classification/application_gzip
                  ...


### File separator and counter `file_counter_separator.sh`
  
🚀 Features

- Automatically detects file types using file --mime-type
- Moves files into corresponding folders named after their MIME type
- Creates a log file (registro_destino.csv) with records of processed files
- Displays progress and execution time

📥 Requisites & How to use:

- Must use a sh compatible enviroment (such as linux, macOS and wsl)
- The file command installed (default in most Linux distributions)
- Read, write, and execute permissions for the directories involved

- Make sure to edit the directories on your computer match the ones on the file<br/>
`source_dir="./Untreated_logs/` => the place where the analyzed files are stored before sorting <br/>
`dest_dir="./sample_classification` => the place where the analyzed files are stored before sorting<br/>
`log_file="registro_destino.csv` => the file with a log repoting what the files were classificated as <br/>

- To execute it, you can either call it from the terminal or make it executable. 

call it by using `sh file_counter_separator.sh` (or your os equivalent sh command) 

📂 Expected Output

If Untreated_logs/ contains:<br/>
- document.pdf<br/>
- image.jpg<br/>
- program.exe<br/>

The script creates:

    sample_classification/ 
    ├── application_pdf/
    │   ├── document.pdf
    ├── image_jpeg/
    │   ├── image.jpg
    ├── application_x-dosexec/
    │   ├── program.exe
    ...

And their respective logs:

    File,           MIME_type,                 Destination Folder
    document.pdf,   application/pdf,           sample_classification/application_pdf
    image.jpg,      image/jpeg,                sample_classification/image_jpeg
    program.exe,    application/x-dosexec,     sample_classification/application_x-dosexec



## Graphs and analysis `graph_analyzer_used_graphs.ipynb`

🚀 Features

- Reads type counts from `./TypeCounts`
- Generate graphics and tables for statystical analysis of the generated logs. <b>Be aware that this notebook was made to account for the file types found in the packages I encountered. If you are analyzing diffent samples, some functions will need to be adjusted to work with your logs.</b>


📥 Requisites & How to use:

- ipynotebook interpreter compatibile with pandas, matplotlib, numpy and seaborn library installed is required. Running python locally is strongly encouraged.

- Locate the TypeCounts folder (or wherever your equivalent folder is) and run the cells inside the notebok.  

📂 Output

The output will vary between cells, but each cell is expected to print a variety of informations ranging from direct information on mime counts and it's origins to pergentage pie graphs.
