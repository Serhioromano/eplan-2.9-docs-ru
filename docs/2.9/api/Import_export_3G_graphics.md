# Import/export 3D graphics

### Export 

Export 3D graphics is possible to STEP or VRML format : 

Export3D::ProjectToStep - exports all installation spaces from a project 

Export3D::InstallationSpacesToStep - exports installation spaces 

Export3D::ProjectToVrml - exports all installation spaces from a project 

Export3D::InstallationSpacesToVrml - exports installation spaces 

### Import 

The item data must be available in the common international STEP format (Standard for the Exchange of Product model data). 

A new layout space is generated for each import, and is given the name of the imported STEP file 

C# |  Copy Code  
---|---  
      
    
    InstallationSpace oInstallationSpace = new Import().Graphics3D(oProject, "c:\\temp\\BK3100\\BK3xxx.stp");
