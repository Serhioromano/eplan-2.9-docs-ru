# Project.CablingDirty
Event when cabling gets dirty

 

 

**Example**

```csharp
m_EventHandler = new EventHandler("Project.CablingDirty");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "Project.CablingDirty was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
