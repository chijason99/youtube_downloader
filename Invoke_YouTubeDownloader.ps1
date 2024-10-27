function Invoke-YouTubeDownloader{
    param(
        [Parameter(Mandatory=$true)]
        [string] $YoutubeLink,
        [switch] $MP3Only
    )

    $PythonScriptPath = "path_to_your_python_script";
    $PythonScript = ".\youtube-downloader.py";
    $Arguments = @($YoutubeLink);

    if ($MP3Only){
        $Arguments += "--mp3-only";
    }

    Set-Location -Path $PythonScriptPath;

    & .\venv\Scripts\activate

    & python $PythonScript @Arguments

    & deactivate

    Set-Location -Path $PWD
}
