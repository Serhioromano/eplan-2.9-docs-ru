# Pre-planning macro

For Pre-planning module, there was created a new class which represents macros : PrePlanningMacro

**Creating these macros is following:**

```csharp
string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
PrePlanningMacro oPrePlanningMacro = new PrePlanningMacro();
oPrePlanningMacro.Create(new[] {oPlanningSegment1, oPlanningSegment2}, strMacroPath, oMultiLangString);
```

Inserting macros requires such parameters as parent planning segment, path to macro and project object:

```csharp
string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
StorableObject[] arrInsertedPlaObjects = new Insert().PrePlanningMacro(strMacroPath, m_oTestProject, oPlanningSegment1);
```

