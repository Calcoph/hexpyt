def remove_namespaces(lines: list[str]) -> list[str]:
    final_lines = []
    namespace_lines = []
    in_namespace = False
    opening_brackets = None
    indentation_length = None
    for line in lines:
        if "namespace" in line:
            in_namespace = True
            if "{" in line:
                opening_brackets = 1
            else:
                opening_brackets = None
        else:
            if in_namespace:
                if "}" in line:
                    opening_brackets -= 1
                    if opening_brackets == 0:
                        line = line.replace("}", "")
                        if len(line) > indentation_length:
                            namespace_lines.append(line[indentation_length:])
                        else:
                            namespace_lines.append(line)
                        in_namespace = False
                        opening_brackets = None
                        indentation_length = None
                        final_lines.extend(remove_namespaces(namespace_lines))
                        namespace_lines = []
                    else:
                        if len(line) > indentation_length:
                            namespace_lines.append(line[indentation_length:])
                        else:
                            namespace_lines.append(line)
                else:
                    if opening_brackets is None:
                        if "{" in line:
                            opening_brackets = 0
                    if opening_brackets is None:
                        continue
                    if "{" in line:
                        opening_brackets += 1
                    if indentation_length is None:
                        i = 0
                        found = False
                        while line[i] != "\n" and not found:
                            if line[i] != " " and line[i] != "\t":
                                found = True
                            else:
                                i += 1
                        if found:
                            indentation_length = i
                    if indentation_length is None:
                        continue
                    if len(line) > indentation_length:
                        namespace_lines.append(line[indentation_length:])
                    else:
                        namespace_lines.append(line)
            else:
                final_lines.append(line)

    return final_lines
