if FORMAT:match 'latex' then
    function Image(elem)
        if string.find(elem.src, "fplogo") then
            return elem
        end
        -- if not elem.caption then
        -- end
        if pcall(function()
            x = '' .. table.concat(elem.caption)
        end) then
            return {pandoc.RawInline('latex', '\\begin{center}'), elem, pandoc.RawInline('latex', '\\end{center}')}
        else
            return elem
        end
    end
end
function dump(o)
    if type(o) == 'table' then
        local s = '{ '
        for k, v in pairs(o) do
            if type(k) ~= 'number' then
                k = '"' .. k .. '"'
            end
            s = s .. '[' .. k .. '] = ' .. dump(v) .. ','
        end
        return s .. '} '
    else
        return tostring(o)
    end
end
