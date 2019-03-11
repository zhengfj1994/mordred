from rdkit import Chem


def generate_mopac_input(mol, fp, condition="PM3 MMOK", confId=-1):
    fc = Chem.GetFormalCharge(mol)
    conf = mol.GetConformer(confId)
    with fp:
        fp.write(" ".join(condition.split("\n")) + " XYZ CHARGE={}\n\n\n".format(fc))
        for i in range(mol.GetNumAtoms()):
            a = mol.GetAtomWithIdx(i)
            f = int(not (a.GetBoolProp("Fixed") if a.HasProp("Fixed") else False))
            x, y, z = conf.GetAtomPosition(i)
            fp.write("{} {} {} {} {} {} {}\n".format(a.GetSymbol(), x, f, y, f, z, f))


def main():
    from rdkit.Chem import AllChem as Chem
    import sys

    mol = Chem.AddHs(Chem.MolFromSmiles(sys.stdin.read()))
    Chem.EmbedMolecule(mol)
    Chem.MMFFOptimizeMolecule(mol)
    generate_mopac_input(mol, sys.stdout)


if __name__ == "__main__":
    main()