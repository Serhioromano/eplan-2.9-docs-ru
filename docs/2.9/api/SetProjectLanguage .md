# SetProjectLanguage

     Action name = SetProjectLanguage
     Set project languages for read-write and read-only projects.
    

   

 

Parameter | Description 

---|--- 

PROJECTNAME |

   

   

    Full project name. The project has to be open.
     

 

DISPLAY |

   

   

    Display language(s) separated by ;
     

 

VARIABLE |

   

   

    Variable project language
     

 

SOURCE |

   

   

    Source language
     

 

 

Remarks
   

   

      The action does not translate the strings, it just changes the display settings.
    

   

 

**Example**

```
SetProjectLanguage /DISPLAY:en_US;de_DE /VARIABLE:en_US
```
