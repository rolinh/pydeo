<%inherit file="../layouts/application.tpl"/>
<div class="row-fluid">
    <div class="bt-group">
        <!--
        <a class="btn" href="#"><input type="checkbox"></input></a>
        <a class="btn dropdown-toggle" data-toggle="dropdown" href="#"><span class="caret"></span></a>
        -->
        <button class="btn" type="submit"><i class="icon-repeat"></i> Reload</button>
    </div>
    <table class="table table-striped table-bordered table-hover table-condensed">
        <thead>
            <tr>
                <th>
                    Movies
                </th>
            </tr>
        </thead>
        <tbody>
        % for m in movies_title:
            <tr>
                <td class="td-wrap">${m}</td>
            </tr>
        % endfor
        </tbody>
    </table>

</div> <!-- row-fluid -->
