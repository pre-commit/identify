from identify import cli


def test_identify_cli(capsys):
    ret = cli.main(('setup.py',))
    out, _ = capsys.readouterr()
    assert ret == 0
    assert out == '["file", "non-executable", "python", "text"]\n'


def test_identify_cli_filename_only(capsys):
    ret = cli.main(('setup.py', '--filename-only'))
    out, _ = capsys.readouterr()
    assert ret == 0
    assert out == '["python", "text"]\n'


def test_identify_cli_filename_only_unidentified(capsys):
    ret = cli.main(('x.unknown', '--filename-only'))
    out, _ = capsys.readouterr()
    assert ret == 1
    assert out == ''


def test_file_not_found(capsys):
    ret = cli.main(('x.unknown',))
    out, _ = capsys.readouterr()
    assert ret == 1
    assert out == 'x.unknown does not exist.\n'
