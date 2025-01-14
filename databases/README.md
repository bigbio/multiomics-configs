## Databases

This directory contains the databases used in the project. The databases are stored in fasta files with extensions fasta or fa.

### Contaminats databases

- [contaminants.fasta](contaminants.fasta): A database of common contaminants in proteomics experiments. This database is used to filter out common contaminants from the search results. It is the merge of crap-202105.fasta and contaminants-mq-202105.fasta from the [MaxQuant](https://www.maxquant.org/) software.

- [contaminants-202105-uniprot.fasta](contaminants-202105-uniprot.fasta): Based on the contaminants.fasta file, this database contains only the contaminants that have a UniProt accession number.

- [contaminants-202105-uniprot-description.fasta](contaminants-202105-uniprot-description.fasta): Based on the contaminants-202105-uniprot.fasta file, this database contains the contaminants with the UniProt accession number and the protein description.

### Decoy and Entrapment databases

We use the [FDRBench](https://github.com/Noble-Lab/FDRBench) to generate the decoy and entrapment databases for the DDA and DIA searches. 

#### DDA database generation: 

```bash 
$ java -jar fdrbench-0.0.2/fdrbench-0.0.2.jar -level protein -db {database_name}.fasta -o {database_name_output}.fasta -I2L -fix_nc c -check -decoy -decoy_label DECOY_ -decoy_pos 0 -entrapment_label ENTRAP_ -entrapment_pos 0
```

The following command line will generate an entrapment protein (prefix: `ENTRAP_`) and two decoy proteins (prefix: `DECOY_`) for each target protein.

This command will generate the following proteins for each target protein:

> sp|A0A087X1C5|CP2D7_HUMAN Putative cytochrome P450 2D7 OS=Homo sapiens OX=9606 GN=CYP2D7 PE=5 SV=1
MGLEALVPLAMLVALFLLLVDLMHRHQRWAARYPPGPLPLPGLGNLLHVDFQNTPYCFDQLRRRFGDVFSLQLAWTPVVVLNGLAAVREAMVTRGEDTADRPPAPLYQVLGFGPRSQGVLLSRYGPAWREQRRFSVSTLRNLGLGKKSLEQWVTEEAACLCAAFADQAGRPFRPNGLLDKAVSNVLASLTCGRRFEYDDPRFLRLLDLAQEGLKEESGFLREVLNAVPVLPHLPALAGKVLRFQKAFLTQLDELLTEHRMTWDPAQPPRDLTEAFLAKKEKAKGSPESSFNDENLRLVVGNLFLAGMVTTSTTLAWGLLLMLLHLDVQRGRRVSPGCPLVGTHVCPVRVQQELDDVLGQVRRPEMGDQAHMPCTTAVLHEVQHFGDLVPLGVTHMTSRDLEVQGFRLPKGTTLLTNLSSVLKDEAVWKKPFRFHPEHFLDAQGHFVKPEAFLPFSAGRRACLGEPLARMELFLFFTSLLQHFSFSVAAGQPRPSHSRVVSFLVTPSPYELCAVPR

> ENTRAP_sp|A0A087X1C5|CP2D7_HUMAN
ALGFLMLLLHVMLDVLALAMPELVRQHRAWARNPPLLDDLPLTGPLGFHFPYLQPYCVNQGRRRAAQFLWLFGVTVVLSAGLVVDPNRMTVAERATDDEGRALGVYFPPPLGQPRSSVQGLLRWYPAGRQERRTVFLSSRLGGNLKKFEQACCTAASLEAWALGDQVAERFPRNLGPDLKVGLNTSVASALCRRFEYPDDRLFRGLLQEALDLKGSEFLERLPLVAGVLPPLANHAEVKLVRQFKLTFLEQELHDTLARWQPPPDMTARLFTADLAEKKEKAKSPSSENNFELDGRTFLLLTGDLSLAGTVNLVGMHLTWLVMLLAQVRGRRVVPVGCGLHSCPVTPRDQGEQLVDLVQVRRGGPLAMPAFTVLQMPCVQVELDGHDTHEHTHVSMTRDELGFVQRPLKLVNLSLSTGTTLKDEVAWKKFPRQFAFLVPHHGHDFEKFPSFPEGAALRRAPCEALLGRFQEFFLPALLLSMVQTGHFSAFSRSHPSRVPPVCPESLTAVSYVFLR

> DECOY_sp|A0A087X1C5|CP2D7_HUMAN
VLAHAPLMLGFLMVLAELLVDMLLRQHRWAARLQYVPLPPPGHDPLLLFDTYGGPNCFLQNRRRALWVVLPQGSAVLLAFGFVNDTVRTVMEARGDEADTRFVPPPYPGGALLQRGSLVQSLRAPYWGRQERRSSFVLTRGGLLNKKLAEGFTAEADWSAAQEAVCLQCRFPRDLNGLPKSGLCNAVTSVALRREFPYDDRLFRGQLAEDLLLKEGELFSRAAVELLAPLPGVHLPNVKLVRQFKAFDEHLTLLETLQRAPTPDMPWQRFAELTLADKKEKAKNLSGSPENFDSERTTDLLMSGVGTLQWLFNMLVLLLAVTVHLGALRGRRVGPVHVPGTPVCSCLRDQDQGVVVLQLERRLFHVVLMMGPHGMLHGQVTETHDDTPCPTAEQVASREGDFQLVRPLKSLTNTLLSVTGLKVDAEWKKFPRLPEHAFFHVGDHQFKFALPEPFGASRRCALLPGEARAHELGFLFTVFSLSFFQQASMPLRSPSHRPSAFPYLVVLVVTEPCSR

We fixed the accessions after running the FDRBench to have every prefix `DECOY`, `ENTRAP` or `CONTAM` in the accession and also the name of each protein. For that we runs the script: 

```python
python fdrbench_accessions.py 
```

The `output.fasta` file is the final DDA database and can be renamed to the final name (e.g. `Homo-sapiens-uniprot-reviewed-contam-entrap-decoy-20241105.fasta`).

#### DIA database generation: 

```bash
$ java -jar fdrbench-0.0.2/fdrbench-0.0.2.jar -level protein -db {database_name}.fasta -o {database_name_output}.fasta -I2L -diann -uniprot -fix_nc c -check -entrapment_label ENTRAP_ -entrapment_pos 0
```

The following command line will generate an entrapment protein (prefix: `ENTRAP_`) for each target protein:

>sp|A0A087X1C5|CP2D7_HUMAN Putative cytochrome P450 2D7 OS=Homo sapiens OX=9606 GN=CYP2D7 PE=5 SV=1
MGLEALVPLAMLVALFLLLVDLMHRHQRWAARYPPGPLPLPGLGNLLHVDFQNTPYCFDQLRRRFGDVFSLQLAWTPVVVLNGLAAVREAMVTRGEDTADRPPAPLYQVLGFGPRSQGVLLSRYGPAWREQRRFSVSTLRNLGLGKKSLEQWVTEEAACLCAAFADQAGRPFRPNGLLDKAVSNVLASLTCGRRFEYDDPRFLRLLDLAQEGLKEESGFLREVLNAVPVLPHLPALAGKVLRFQKAFLTQLDELLTEHRMTWDPAQPPRDLTEAFLAKKEKAKGSPESSFNDENLRLVVGNLFLAGMVTTSTTLAWGLLLMLLHLDVQRGRRVSPGCPLVGTHVCPVRVQQELDDVLGQVRRPEMGDQAHMPCTTAVLHEVQHFGDLVPLGVTHMTSRDLEVQGFRLPKGTTLLTNLSSVLKDEAVWKKPFRFHPEHFLDAQGHFVKPEAFLPFSAGRRACLGEPLARMELFLFFTSLLQHFSFSVAAGQPRPSHSRVVSFLVTPSPYELCAVPR

>sp|ENTRAP_A0A087X1C5|ENTRAP_CP2D7_HUMAN Putative cytochrome P450 2D7 OS=Homo sapiens OX=9606 GN=ENTRAP_CYP2D7 PE=5 SV=1
VLAHAPLMLGFLMVLAELLVDMLLRQHRWAARLCVHLGDPLFPYLGQGTPPLPYNPLFDQNRRRNGPLDVTVLAAVFSVFWLGAVQLRVAEMTREDADTGRPLQPYFGPAVLGPRQLLSSGVRAWGPYRQERRSSLFTVRGGLLNKKAFEACSCAEEGWALAAQVTDLQRFPRDPLGLNKTSAASVLVLNGCRRFEDPDYRLFRALLGEDQLLKSFEGLERLPHVAVGPLLALAVNPEKLVRQFKETHLTALEFLLDQRPDTMPAPWQRDEFLAATLKKEKAKFSNEGNDSSEPLRNVTTFLMTTVLLAMLHGQLLGLDLVGLWVLSARGRRLVVVTPVCSPPCGGHRDQDLEGQQLVVVRRVMTTTQLSLDGAVPPCDEQLHEGHFTMPAGMHHVVREQLVDGFRPLKGTTLNLLVSTSLKAWVDEKKFPRLVHQFAHPDEFFHGKFLGESAFPPARRPLCLGAAERLAGFTSFPVFEQMSQLFHLASFLRHPSSRVLLPFCVVTVAEYPSPSR

