#define MyAppName "PyInstallApp"
#define MyAppVersion "1.0"
#define MyAppPublisher "Raminhos Industries"
#define MyAppURL "http://www.pedrorarmos.netlify.app/"
#define MyAppExeName "PyInstallerApp.exe"

#define PathApp "D:\GitHub\PythonCourseUdemy\kivy\aulas\Seção 27 - Empacotamento\05 - Empacotamento Kivy"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools{49D20A2C-9819-441B-8446-C918B1598F86} | Generate GUID inside the IDE.)
AppId={{49D20A2C-9819-441B-8446-C918B1598F86}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}

LicenseFile={#PathApp}\license.txt
InfoBeforeFile={#PathApp}\before.txt
InfoAfterFile={#PathApp}\after.txt
OutputDir=D:\GitHub\PythonCourseUdemy\kivy\aulas\Seção 27 - Empacotamento\06 - Inoo Setup\PyInstallAppInstaller
OutputBaseFilename=instalador
SetupIconFile={#PathApp}\icone.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "D:\GitHub\PythonCourseUdemy\kivy\aulas\Seção 27 - Empacotamento\05 - Empacotamento Kivy\dist\PyInstallerApp\PyInstallerApp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\GitHub\PythonCourseUdemy\kivy\aulas\Seção 27 - Empacotamento\05 - Empacotamento Kivy\dist\PyInstallerApp\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
