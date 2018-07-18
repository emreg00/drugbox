# -*- coding: utf-8 -*-

from drugbox import drugbank
from io import StringIO

import unittest


class DrugBoxTestSuite(unittest.TestCase):
    """Several test cases."""

    def setUp(self):
        self.drug = "DB00001"
        self.targets = ["P00734"]
        self.xml = """<?xml version="1.0" encoding="UTF-8"?>
<drugbank xmlns="http://www.drugbank.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.drugbank.ca http://www.drugbank.ca/docs/drugbank.xsd" version="4.3">
<drug type="biotech" created="2005-06-13" updated="2018-03-02">
  <drugbank-id primary="true">DB00001</drugbank-id>
  <drugbank-id>BTD00024</drugbank-id>                                      
  <drugbank-id>BIOD00024</drugbank-id>                                     
  <name>Lepirudin</name>                                                   
  <description>Lepirudin is identical.</description>
  <cas-number>138068-37-8</cas-number>                                     
  <unii>Y43GF64R34</unii>
  <state>liquid</state>                                                    
  <groups>
    <group>approved</group>                                                
  </groups>
  <indication>For the treatment.</indication>
  <pharmacodynamics>Lepirudin is used.</pharmacodynamics>
  <mechanism-of-action>Lepirudin forms a stable. </mechanism-of-action>
  <synonyms>
    <synonym language="" coder="">Hirudin variant-1</synonym>
    <synonym language="" coder="">Lepirudin recombinant</synonym>
  </synonyms>
  <products>
    <product>
      <name>Refludan</name>
      <labeller>Bayer</labeller>
      <ndc-id/>
      <ndc-product-code/>
      <dpd-id>02240996</dpd-id>
      <ema-product-code/>
      <ema-ma-number/>
      <started-marketing-on>2000-01-31</started-marketing-on>
      <ended-marketing-on>2013-07-26</ended-marketing-on>
      <dosage-form>Powder, for solution</dosage-form>
      <strength>50 mg</strength>
      <route>Intravenous</route>
      <fda-application-number/>
      <generic>false</generic>
      <over-the-counter>false</over-the-counter>
      <approved>true</approved>
      <country>Canada</country>
      <source>DPD</source>
    </product>
  </products>
  <international-brands/>
  <mixtures>
    <mixture>
      <name>Refludan</name>
      <ingredients>Lepirudin</ingredients>
    </mixture>
    <mixture>
      <name>Refludan</name>
      <ingredients>Lepirudin</ingredients>
    </mixture>
  </mixtures>
  <drug-interactions>
    <drug-interaction>
      <drugbank-id>DB00977</drugbank-id>
      <name>Ethinyl Estradiol</name>
      <description>The serum concentration of Ethinyl Estradiol can be decreased when it is combined with Lepirudin.</description>
    </drug-interaction>
    <drug-interaction>
      <drugbank-id>DB01357</drugbank-id>
      <name>Mestranol</name>
      <description>The serum concentration of Mestranol can be decreased when it is combined with Lepirudin.</description>
    </drug-interaction>
  </drug-interactions>
  <sequences>
    <sequence format="FASTA">&gt;DB00001 sequence
LVYTDCTESGQNLCLCEGSNVCGQGNKCILGSDGEKNQCVTGEGTPKPQSHNDGDFEEIP
EEYLQ</sequence>
  </sequences>
  <experimental-properties>
    <property>
      <kind>Melting Point</kind>
      <value>65 °C</value>
      <source>Otto, A. &amp; Seckler, R. Eur. J. Biochem. 202:67-73 (1991)</source>
    </property>
    <property>
      <kind>Hydrophobicity</kind>
      <value>-0.777</value>
      <source/>
    </property>
    <property>
      <kind>Isoelectric Point</kind>
      <value>4.04</value>
      <source/>
    </property>
    <property>
      <kind>Molecular Weight</kind>
      <value>6963.425</value>
      <source/>
    </property>
    <property>
      <kind>Molecular Formula</kind>
      <value>C287H440N80O110S6</value>
      <source/>
    </property>
  </experimental-properties>        
    <external-identifiers>
    <external-identifier>
      <resource>PubChem Substance</resource>
      <identifier>46507011</identifier>
    </external-identifier>
    <external-identifier>
      <resource>KEGG Drug</resource>
      <identifier>D06880</identifier>
    </external-identifier>
    <external-identifier>
      <resource>ChEMBL</resource>
      <identifier>CHEMBL1201666</identifier>
    </external-identifier>
  </external-identifiers>
  <targets>
    <target>
      <id>BE0000048</id>
      <name>Prothrombin</name>
      <organism>Human</organism>
      <actions>
        <action>inhibitor</action>
      </actions>
      <references>
        <articles>
          <article>
            <pubmed-id>10505536</pubmed-id>
            <citation>Turpie AG: Anticoagulants in acute coronary syndromes. Am J Cardiol. 1999 Sep 2;84(5A):2M-6M.</citation>
          </article>
        </articles>
        <textbooks/>
        <links/>
      </references>
      <known-action>yes</known-action>
      <polypeptide id="P00734" source="Swiss-Prot">
    <name>Prothrombin</name>
    <general-function>Thrombospondin receptor activity</general-function>
    <specific-function>Thrombin, which cleaves bonds after Arg and Lys, converts fibrinogen to fibrin and activates factors V, VII, VIII, XIII, and, in complex with thrombomodulin, protein C. Functions in blood homeostasis, inflammation and wound healing.</specific-function>
    <gene-name>F2</gene-name>
    <locus>11p11-q12</locus>
    <cellular-location>Secreted</cellular-location>
    <transmembrane-regions/>
    <signal-regions>1-24</signal-regions>
    <theoretical-pi>5.7</theoretical-pi>
    <molecular-weight>70036.295</molecular-weight>
    <chromosome-location>11</chromosome-location>
    <organism ncbi-taxonomy-id="9606">Human</organism>
    <external-identifiers>
      <external-identifier>
        <resource>HUGO Gene Nomenclature Committee (HGNC)</resource>
        <identifier>HGNC:3535</identifier>
      </external-identifier>
      <external-identifier>
        <resource>UniProtKB</resource>
        <identifier>P00734</identifier>
      </external-identifier>
      <external-identifier>
        <resource>UniProt Accession</resource>
        <identifier>THRB_HUMAN</identifier>
      </external-identifier>
    </external-identifiers>
    <synonyms>
      <synonym>3.4.21.5</synonym>
      <synonym>Coagulation factor II</synonym>
    </synonyms>
    <amino-acid-sequence format="FASTA">&gt;lcl|BSEQ0016004|Prothrombin
MAHVRGLQLPGCLALAALCSLVHSQHVFLAPQQARSLLQRVRRANTFLEEVRKGNLEREC
RIRITDNMFCAGYKPDEGKRGDACEGDSGGPFVMKSPFNNRWYQMGIVSWGEGCDRDGKY
GFYTHVFRLKKWIQKVIDQFGE</amino-acid-sequence>
    <gene-sequence format="FASTA">&gt;lcl|BSEQ0016005|Prothrombin (F2)
ATGGCGCACGTCCGAGGCTTGCAGCTGCCTGGCTGCCTGGCCCTGGCTGCCCTGTGTAGC
CGCTGGTATCAAATGGGCATCGTCTCATGGGGTGAAGGCTGTGACCGGGATGGGAAATAT
GGCTTCTACACACATGTGTTCCGCCTGAAGAAGTGGATACAGAAGGTCATTGATCAGTTT
GGAGAGTAG</gene-sequence>
    <pfams>
      <pfam>
        <identifier>PF00594</identifier>
        <name>Gla</name>
      </pfam>
      <pfam>
        <identifier>PF00051</identifier>
        <name>Kringle</name>
      </pfam>
    </pfams>
    <go-classifiers>
      <go-classifier>
        <category>component</category>
        <description>blood microparticle</description>
      </go-classifier>
      <go-classifier>
        <category>component</category>
        <description>extracellular matrix</description>
      </go-classifier>
      <go-classifier>
        <category>component</category>
        <description>Golgi lumen</description>
      </go-classifier>
    </go-classifiers>
  </polypeptide>
    </target>
  </targets>
  <enzymes/>
  <carriers/>
  <transporters/>
</drug>
</drugbank>"""


    def test_Parser(self):
        parser = drugbank.DrugBankXMLParser(StringIO(self.xml))
        parser.parse()
        drug_to_uniprots = parser.get_targets(target_types = set(["target", "enzyme"]), only_paction=False)
        self.assertEqual(drug_to_uniprots[self.drug], set(self.targets))


if __name__ == '__main__':
    unittest.main()
