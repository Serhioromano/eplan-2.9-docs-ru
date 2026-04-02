# plcservice

    Exports/imports PLC data using the specified converter.
    

  
Parameter | Description  
---|---  
TYPE | 
    
    
    Type of task to be performed by the action
    BUSDATAEXPORT: Bus data export.
    BUSDATAIMPORT: Bus data import.
    GENERATEPLCSCHEMATIC: Schematics generation.
    EXPORTADDRESSOVERVIEW: Address overview export.
      
  
PROJECTNAME | 
    
    
    Project name with full path.
      
  
LANGUAGE | 
    
    
    Language identifier 
    This parameter is only effective with the following values of the TYPE parameter: BUSDATAEXPORT, BUSDATAIMPORT
      
  
CONVERTERID | 
    
    
    Identification for busdata exporter. Values are:
    • PlcDcExchangerBeckhoffTC3AML = Beckhoff TwinCAT 3
    • PlcDcExchangerBoschAML = Bosch Nexeed Automation
    • PlcDcExchangerLogiCals3AML = logi.cals logi.CAD 3
    • PlcDcExchangerMitsubishiAML = Mitsubishi iQ Works
    • PlcDcExchangerPhoenixContactAML = Phoenix Contact PLCnext Engineer 2019
    • PlcDcExchangerRockwellArchitectAML = Rockwell Automation Studio 5000
    • PlcDcExchangerSiemensTIAAML = Siemens SIMATIC STEP 7 TIA-Portal 14SP1
    • PlcDcExchangerSiemensTIA15AML = Siemens SIMATIC STEP 7 TIA-Portal 15
    • PlcDcExchangerSiemensTIA151AML = Siemens SIMATIC STEP 7 TIA Portal 15.1
    • PlcDcExchangerSiemensTIA16AML = Siemens SIMATIC STEP 7 TIA Portal 16
    • PlcDcExchangerSiemensTSTAML = Siemens TIA Selection Tool
    • PlcDcAMLExchangerGeneral = Eplan Electric P8 AML-format
    • PlcDcXMLExchangerABB = ABB Automation Builder
    • PlcDcXMLExchangerBandR = B and R Automation Studio
    • PlcDcXMLExchangerBeckhoff = Beckhoff TwinCAT 2.10/2.11
    • PlcDcXMLExchangerLogiCals = logi.cals logi.CAD
    • PlcDcXMLExchangerMitsubishi = Mitsubishi GX-Works2
    • PlcDcXMLExchangerRexroth = Bosch Rexroth Indra Works
    • PlcDcXMLExchangerSchneider = Schneider Unity Pro XL
    • PlcDcXMLExchangerSiemens = Siemens SIMATIC STEP 7 5.6
    • PlcDcXMLExchangerUniversal = Eplan Electric P8 PLC standard exchange format
    • XMLRockwellExchanger = Rockwell Studio 5000 Architect 20/21
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAEXPORT, BUSDATAIMPORT
      
  
CONFIGURATIONPROJECT | 
    
    
    The name of the PLC configuration data set to export. 
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAEXPORT, EXPORTADDRESSOVERVIEW
      
  
DESTINATIONFILE | 
    
    
    Destination file for data export.
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAEXPORT, EXPORTADDRESSOVERVIEW
      
  
SOURCEFILE | 
    
    
    Source file for data import.
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAIMPORT.
      
  
OVERWRITE | 
    
    
    If the output file already exists, this parameter specifies      whether it should be overwritten.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAEXPORT.
      
  
IMPORTMATCH | 
    
    
    Matching options for PLC data import. 
    The import process tries to match imported objects with those existing in the project.
    Based on the option selected, the matching may be performed by internal object ids or by objects' identifying names.
    If an imported object is matched with an existing function, properties of the existing function will be updated whereas for unmatched imported objects, new functions will be created in the project.
    The options are:
    0 = Match by internal object ids.
    1 = Match by identifying names. Note: in this case, a comparison dialog may be displayed for the user to individually selecting some function to update.
    2 = Don't match. Create new functions for all imported objects.
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAIMPORT.
      
  
SHOWCOMPAREDLG | 
    
    
    Shows compare dialog.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:BUSDATAIMPORT.
      
  
CONFIGFILE | 
    
    
    A path to a  configuration file for schematics generation.
    This parameter is only effective with the following values of the TYPE parameter:GENERATEPLCSCHEMATIC.
      
  
SINGLELINEPAGES | 
    
    
    If set, single-line pages will be generated.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:GENERATEPLCSCHEMATIC.
      
  
MULTILINEPAGES | 
    
    
    If set, multi-line pages will be generated.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:GENERATEPLCSCHEMATIC.
      
  
OVERVIEWS | 
    
    
    If set, overview pages will be generated.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:GENERATEPLCSCHEMATIC.
      
  
RACKOVERVIEWS | 
    
    
    If set, rack overview pages will be generated.
    Possible values: '0' - No (default), '1' - Yes.
    This parameter is only effective with the following values of the TYPE parameter:GENERATEPLCSCHEMATIC.
      
  
PLCSTATION | 
    
    
    The name of the PLC station name to export.
    This parameter is only effective with the following values of the TYPE parameter:EXPORTADDRESSOVERVIEW
      
  
PLCCPU | 
    
    
    The name of the PLC CPU name to export.
    This parameter is only effective with the following values of the TYPE parameter:EXPORTADDRESSOVERVIEW
      
  
  
**Example**

```
Bus data export:

plcservice 
                /TYPE:BUSDATAEXPORT
                /CONFIGURATIONPROJECT:Schneider-Electric
                /DESTINATIONFILE:"c:\tempdir\plcservice_export_1.xef"
                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\ESS_Sample_Project.elk" 
                /LANGUAGE:de_DE
                /CONVERTERID:PlcDcXMLExchangerSchneider
                /OVERWRITE:1

Bus data import:

plcservice 
                /TYPE:BUSDATAIMPORT
                /SOURCEFILE:"c:\tempdir\plcservice_export_2.pbf"
                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\ESS_Sample_Project.elk" 
                /LANGUAGE:de_DE
                /CONVERTERID:PlcDcXMLExchangerUniversal

Schematics generation:

plcservice 
                /TYPE:GENERATEPLCSCHEMATIC
                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\ESS_Sample_Project.elk" 
                /CONFIGFILE:"c:\tempdir\schematics_generation_config.xml"
                /SINGLELINEPAGES:1
                /MULTILINEPAGES:1

Address overview export:

plcservice 
                /TYPE:EXPORTADDRESSOVERVIEW
                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\ESS_Sample_Project.elk" 
                /CONFIGURATIONPROJECT:"CAx_AML_Drive_00"
                /PLCSTATION:"S71500/ET200MP station_1"
                /PLCCPU:"1"
                /DESTINATIONFILE:"c:\tempdir\address_overview_export.csv"
```
