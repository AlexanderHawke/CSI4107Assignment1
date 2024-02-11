Text collection
--------------

The collection includes 79923 documents, grouped in 322 files, from the Associated Press, 
1988. The <TEXT> field should be indexed for each document. 
Optionally, the <HEAD> can be used. In the DOCNO field, 
the code uniquely identifies the document. An example of code is AP880212-0004


Queries (Topics)
---------------

There are 50 Test Topics. The topics have a number, a title, a 
description and a longer explanation called narrative. You can use the 
content of the <title>, <desc>, and <narr> fields for each query to 
extract keywords (or, if you prefer, only <title>, or <title> and <desc>).


Relevance Judgments 
-------------------------------------------

To facilitate information retrieval experimentation, the ideal 
solution for the Test Topics is given in qrels1-50ap.txt 
The file contains binary relevance scores in the format used by 
trec_eval:
        
TopicNumber DummyColumn DOCNO BinaryRelevance

where DummyColumn is always zero, DOCNO is in the document name
as explained above and BinaryRelevance is either 0 or 1.  The
relevance scores are sorted by topic, in ascending order.


Examples:

Document 
-----------------
<DOC>
<DOCNO> AP880212-0004 </DOCNO>
<FILEID>AP-NR-02-12-88 1637EST</FILEID>
<1ST_LINE>r w AM-PeanutSupports     02-12 0155</1ST_LINE>
<2ND_LINE>AM-Peanut Supports,150</2ND_LINE>
<HEAD>Peanut Price Supports Will Go Higher This Year</HEAD>
<DATELINE>WASHINGTON (AP) </DATELINE>
<TEXT>
   Price supports for peanuts grown under 1988
quotas will be $615.27 per ton, an increase of $7.80 from last
year, the Agriculture Department said Friday.
   Deputy Secretary Peter C. Myers said the increase was required
by a formula in the law which takes rising production costs into
consideration.
   The annual quota is set at a level equal to the estimated
quantity of peanuts that will be needed for domestic edible uses,
seed and related purposes.
   Production of non-quota peanuts, which can be grown for peanut
oil and meal, and for export, will be supported at $149.75 per ton,
unchanged from last year, Myers said.
   In setting the support for non-quota peanuts, officials are
required to consider certain factors, including the demand for oil
and meal, the expected prices for other vegetable oils and meals,
and the foreign demand for peanuts.
</TEXT>
</DOC>



Query (topic)
-------------
<num>1
<title>Coping with overcrowded prisons
<desc>
The document will provide information on jail and prison overcrowding and 
how inmates are forced to cope with those conditions; or it will reveal 
plans to relieve the overcrowded condition.
<narr>
A relevant document will describe scenes of overcrowding that have 
become all too common in jails and prisons around the country.  The 
document will identify how inmates are forced to cope with those 
overcrowded conditions, and/or what the Correctional System is doing, 
or planning to do, to alleviate the crowded condition.
</top>


Relevance judgements
--------------------
3 0 AP880731-0027 0
3 0 AP880803-0028 0
3 0 AP880803-0211 1
3 0 AP880804-0010 0
...