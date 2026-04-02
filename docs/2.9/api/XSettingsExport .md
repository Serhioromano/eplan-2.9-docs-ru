# XSettingsExport

     Exports settings to a xml-file.
     
    

  
Parameter | Description  
---|---  
node | 
    
    
    Path of a setting node (without PROJECT)
      
  
XMLFile | 
    
    
    Full name of a xml-file
      
  
prj | 
    
    
    Project (has to be open)
      
  
  
Remarks


  
Example
    
    
       XSettingsExport /node:USER /XMLFile:c:\my_user.xml
       
    

  

    
    
       XSettingsExport /node:STATION /XMLFile:c:\my_station.xml
       
    

  

    
    
       XSettingsExport /node:COMPANY /XMLFile:c:\my_company.xml
       
    

  

    
    
       XSettingsExport /node:USER.DIALOGSETTINGS /XMLFile:c:\my_dialog_settings.xml
       
    

  

    
    
       XSettingsExport /prj:ESS_Sample_Project /XMLFile:c:\my_project.xml
       
    

  

    
    
       XSettingsExport /prj:ESS_Sample_Project /node:XSbGui.CustomSymbols /XMLFile:c:\my_custom_symbols.xml
