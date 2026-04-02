# EPLAN Remoting

EPLAN Remoting is a part of API which enables user to connect to an EPLAN Platform variant and control it in remote way. Internally it uses WCF technology.

The connection is established from client application (a .Net program written by API user) to existing EPLAN instance which is available in network.

The condition is that EPLAN variant is started as remoting server (without /NoRemoting parameter).

**EPLAN Remoting consits of following libraries:**

  * `Eplan.EplApi.RemoteClientu.dll` (namespace [Eplan.EplApi.RemoteClient](Eplan_EplApi_RemoteClient.md))
  * `Eplan.EplApi.Remotingu.dll` (namespace [Eplan.EplApi.Remoting](Eplan_EplApi_Remoting.md))

Both dlls are stored in EPLAN Platform bin folder. Bellow are examples how to use it.

**Establishing connection with localhost:**

```csharp
EplanRemoteClient m_pClient = new EplanRemoteClient();
bool bConnected = m_pClient.Connect("localhost", "49155");   //default port for EPLAN instance is 49155
```

**Establishing connection with a remote server:**

```csharp
EplanRemoteClient m_pClient = new EplanRemoteClient();
bool bConnected = m_pClient.Connect("remote_server", "49155", new TimeSpan(0, 0, 0, 5));   //wait 5 seconds
```

**Start EPLAN instance locally from a client:**

```csharp
List<EplanServerData> oInstalledEplanVersions = new List<EplanServerData>(); m_pClient.GetInstalledEplanVersionsOnLocalMachine(out oInstalledEplanVersions); EplanServerData oConnected = oEplanRemoteClient.StartEplan(oInstalledEplanVersions[0].EplanPath);
```

To make sure that EPLAN Server was started, please check registry key HKEY_CURRENT_USER\Software\EPLAN\RemoteServer\<port_number>

**Calling an action:**

```csharp
bool oResp = m_pClient.ExecuteAction("XPartsManagementStart");
```

**Calling action in asynchronous mode:**

```csharp
m_pClient.SynchronousMode = false; m_pClient.ExecuteAction("XPartsManagementStart");
```

In this case program starts action and continues.

Calling action in synchronous mode, for example to get input from user:

```csharp
m_pClient.SynchronousMode = true; CallingContext oCallingContext = new CallingContext(); m_pClient.ExecuteAction("XPamSelectPart", ref oCallingContext);
```

In this case program waits until action execution is finished.

**Listing servers on a local machine:**

```csharp
List<EplanServerData> oActiveEplanVersions = new List<EplanServerData>();
m_pClient.GetActiveEplanServersOnLocalMachine(out oActiveEplanVersions);
foreach (EplanServerData oVersion in oActiveEplanVersions)
   Console.WriteLine(oVersion.EplanVariant + "," + oVersion.EplanVersion + "," + oVersion.ServerPort);

** Getting installed servers:**

```

```csharp
List<EplanServerData> oInstalledEplanVersions = new List<EplanServerData>();
m_pClient.GetInstalledEplanVersionsOnLocalMachine(out oInstalledEplanVersions);
foreach (EplanServerData oVersion in oInstalledEplanVersions)
   Console.WriteLine(oVersion.EplanVariant + "," + oVersion.EplanVersion + "," + (oVersion.Is64Bit ? "64" : "32");
```

**Making selection:**

```csharp
StringCollection oObjects = new StringCollection(); oObjects.Add(@"17/688");
EplanResponse oResponse = m_pClient.SelectEplanObjects(@"$(MD_PROJECTS)\ESS_Sample_Project.elk", oObjects, true);
```

**Disconnection:**

```csharp
m_pClient.Disconnect();
```

