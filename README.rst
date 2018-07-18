DrugBox: Parsers for various drug info databases
================================================

Python 3 parsers for the following resources:

* `DrugBank <http://drugbank.ca>`_

TODO (add parsers for):
|`ChEMBL <https://www.ebi.ac.uk/chembldb>`_
|`STITCH <http://stitch.embl.de/>`_

Example usage: ::

from drugbox import drugbank
file_name = "drugbank.xml"
out_file = "targets.tsv"
# Output uniprot ids of (pharmacological) targets of drugs
drugbank.output_data(file_name, out_file, target_type_list = ["target"])
# Output gene symbols of all targets (enzymes, transporters, carriers, etc) of drugs along with the known action information
drugbank.output_target_info(file_name, out_file)

---------------

See `toolbox repository <https://github.com/emreg00/toolbox>`_ for a related package with other parsers (DrugBank, ChEMBL and STITCH) 
for Python 2 and extra functionality.

