function Invoke-YouTubeDownloader{
    param(
        [Parameter(Mandatory=$true)]
        [string] $YoutubeLink,
        [switch] $MP3Only
    )

    $PythonScriptPath = "C:\Users\JASON\Desktop\web dev\projects\youtube-donwloader";
    $PythonScript = ".\youtube-downloader.py";
    $Arguments = @($YoutubeLink);

    if ($MP3Only){
        $Arguments += "--mp3-only";
    }

    Set-Location -Path $PythonScriptPath;

    & .\.venv\Scripts\activate

    & python $PythonScript @Arguments

    & deactivate

    Set-Location -Path $PWD
}
